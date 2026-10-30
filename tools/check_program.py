#!/usr/bin/env python3
"""Consistency checker for the Burn and Churn Coffee security program.

Compares every repository in the program against the canonical org data in
00-company-profile/org/ (people, systems, vendors) and against itself
(IDs, links, control counts), and scans for secrets. See CLAUDE.md section 10.

Usage (from the hub root, with the labs cloned alongside it):
    python tools/check_program.py --hub . --iam ../IAM-Access-Review-Lab --vra ../Vendor-Risk-Assessment-Lab

With only --hub, the cross-repository checks are skipped (this is what CI runs).
Exit code 0 means every check passed; 1 means at least one finding.
Standard library only.
"""
import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

HUB_URL = "github.com/MgnCoding2020/grc-paper-project-coffee-shop"

# Role names used in older records, mapped to the roles in people.csv (see org/roles.md).
ROLE_ALIASES = {
    "Business Owner": "Owner",
    "Owner": "Owner",
    "Store Manager": "Store Manager",
    "Manager": "Store Manager",
    "Shift Leader": "Shift Leader",
    "Employee": "Barista",
    "Barista": "Barista",
    "IT Technician": "IT Technician",
}

# System names used in evidence, mapped to systems.csv IDs.
SYSTEM_ALIASES = {
    "Toast POS": "SYS-001",
    "Google Workspace": "SYS-002",
    "Google Admin Console": "SYS-003",
    "xtraCHEF": "SYS-004",
    "QuickBooks Online": "SYS-005",
    "Northwind Payroll Services": "SYS-006",
    "Network Admin": "SYS-007",
    "Microsoft Entra ID": "SYS-010",
}

SCANNED_SUFFIXES = {".md", ".csv", ".txt", ".py", ".ps1", ".json", ".yml", ".yaml", ".example"}
STORE_ROLES = {"Owner", "Store Manager", "Shift Leader", "Barista"}

SECRET_PATTERNS = {
    "GUID (tenant, client or object ID)": re.compile(
        r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
    "real *.onmicrosoft.com domain": re.compile(r"\b[a-z0-9-]+\.onmicrosoft\.com\b", re.I),
    "IPv4 address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "access token (JWT)": re.compile(r"\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}"),
    "Stripe API key": re.compile(r"\b(?:sk|rk|pk)_(?:live|test)_[A-Za-z0-9]{10,}"),
    # Any address outside the fictional domain (and example domains) could be a real test mailbox
    "email address outside the fictional domain": re.compile(
        r"\b[\w.+-]+@(?!burnandchurncoffee\.com\b|example\.(?:com|org|net)\b)[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b"),
}
PERSONAL_DATA_PATTERNS = {
    "SSN-shaped number": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "phone number": re.compile(r"\(?\b\d{3}\)?[-. ]\d{3}[-.]\d{4}\b"),
}


class Report:
    """Collects findings per check and prints a summary."""

    def __init__(self):
        self.results = []  # (number, name, status, findings)

    def add(self, number, name, findings, skipped=None):
        if skipped:
            self.results.append((number, name, "SKIPPED", [skipped]))
        else:
            self.results.append((number, name, "PASS" if not findings else "FAIL", findings))

    def print(self):
        for number, name, status, findings in self.results:
            label = status if status != "FAIL" else f"FAIL ({len(findings)})"
            print(f"[{number}] {name}: {label}")
            for line in findings:
                print(f"      - {line}")
        counts = {s: sum(1 for r in self.results if r[2] == s) for s in ("PASS", "FAIL", "SKIPPED")}
        total = sum(len(r[3]) for r in self.results if r[2] == "FAIL")
        print()
        print(f"Summary: {counts['PASS']} passed, {counts['FAIL']} failed, {counts['SKIPPED']} skipped; "
              f"{total} finding(s).")
        return counts["FAIL"]


# ---------------------------------------------------------------- helpers

def read_text(path):
    return Path(path).read_text(encoding="utf-8-sig", errors="replace")


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def md_tables(path):
    """Return every markdown table in a file as a list of dicts (header -> cell)."""
    tables, header, rows = [], None, []
    for line in read_text(path).splitlines():
        line = line.strip()
        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if header is None:
                header = cells
            elif set("".join(cells)) <= set("-: "):
                continue
            else:
                rows.append(dict(zip(header, cells)))
        elif header is not None:
            tables.append(rows)
            header, rows = None, []
    if header is not None:
        tables.append(rows)
    return tables


def table_with(path, column):
    """The first table in a file that has the given column."""
    for rows in md_tables(path):
        if rows and column in rows[0]:
            return rows
    return []


def tracked_files(repo):
    """Files git tracks in a repo (falls back to every file if git is unavailable)."""
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files"], capture_output=True,
                             text=True, check=True).stdout
        return [Path(repo) / p for p in out.splitlines()]
    except (OSError, subprocess.CalledProcessError):
        return [p for p in Path(repo).rglob("*") if p.is_file() and ".git" not in p.parts]


def rel(path, root):
    return Path(path).relative_to(root).as_posix()


def strip_code(text):
    """Remove fenced code blocks and inline code, so examples don't count as references."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


# ---------------------------------------------------------------- org data

class Org:
    def __init__(self, hub):
        org = Path(hub) / "00-company-profile" / "org"
        self.people = read_csv(org / "people.csv")
        self.systems = read_csv(org / "systems.csv")
        self.vendors = read_csv(org / "vendors.csv")
        contacts = org / "vendor-contacts.csv"
        self.contacts = read_csv(contacts) if contacts.exists() else []
        self.by_name = {p["display_name"]: p for p in self.people}
        self.contact_names = {c["display_name"] for c in self.contacts}
        self.by_upn = {p["upn"].lower(): p for p in self.people}
        self.system_ids = {s["system_id"] for s in self.systems}
        self.vendor_ids = {v["vendor_id"] for v in self.vendors}
        self.vendor_names = [v["name"] for v in self.vendors]

    def is_vendor_name(self, name):
        return name in self.contact_names or any(
            name.lower() in v.lower() or v.lower().startswith(name.lower()) for v in self.vendor_names)

    def store_headcount(self):
        return sum(1 for p in self.people
                   if p["role"] in STORE_ROLES and p["employment_status"] == "Active")


# ---------------------------------------------------------------- checks

def check_people(hub, iam, org):
    findings = []
    access = Path(hub) / "07-evidence-pack" / "artifacts"

    def check_identity(value, where):
        value = value.strip()
        if not value:
            return
        if "@" in value:
            if value.lower() not in org.by_upn:
                findings.append(f"{where}: account '{value}' is not a UPN in people.csv")
        elif value not in org.by_name and not org.is_vendor_name(value):
            findings.append(f"{where}: '{value}' is not in people.csv or vendors.csv")

    for name, column in [("access/user-access-review.csv", "Username"),
                         ("access/mfa-status.csv", "User"),
                         ("training/security-training-log.csv", "employee_name")]:
        path = access / name
        if path.exists():
            for i, row in enumerate(read_csv(path), start=2):
                check_identity(row.get(column, ""), f"hub {name}:{i}")

    log = access / "monitoring" / "incident-log.md"
    if log.exists():
        for match in re.finditer(r"^- User:\s*(\S+)", read_text(log), re.M):
            check_identity(match.group(1), "hub monitoring/incident-log.md")

    if iam:
        matrix = Path(iam) / "evidence" / "user-access-matrix.csv"
        for i, row in enumerate(read_csv(matrix), start=2):
            name, role, status = row["User_Name"], row["Role"], row["Employment_Status"]
            where = f"IAM evidence/user-access-matrix.csv:{i}"
            person = org.by_name.get(name)
            if person is None:
                if not org.is_vendor_name(name):
                    findings.append(f"{where}: '{name}' is not in people.csv or vendors.csv")
                continue
            if ROLE_ALIASES.get(role) != person["role"]:
                findings.append(f"{where}: {name} has role '{role}', people.csv says '{person['role']}'")
            if status != person["employment_status"]:
                findings.append(f"{where}: {name} is '{status}', people.csv says '{person['employment_status']}'")
        findings_doc = Path(iam) / "findings" / "access-review-findings.md"
        for match in re.finditer(r"\*\*User:\*\*\s*(.+)", read_text(findings_doc)):
            check_identity(match.group(1), "IAM findings/access-review-findings.md")
    return findings


def check_systems_and_vendors(hub, iam, vra, org):
    findings = []
    access = Path(hub) / "07-evidence-pack" / "artifacts" / "access"
    sources = [(access / "user-access-review.csv", "hub", "System"),
               (access / "mfa-status.csv", "hub", "System")]
    if iam:
        sources.append((Path(iam) / "evidence" / "user-access-matrix.csv", "IAM", "System"))
    for path, repo, column in sources:
        if not path.exists():
            continue
        for i, row in enumerate(read_csv(path), start=2):
            system = row.get(column, "").strip()
            if system and SYSTEM_ALIASES.get(system) not in org.system_ids:
                findings.append(f"{repo} {path.name}:{i}: system '{system}' does not map to systems.csv")

    inventory = Path(hub) / "02-risk-management" / "vendor-risk-management" / "vendor-inventory.md"
    listed = {row["Vendor ID"] for row in table_with(inventory, "Vendor ID")}
    for vendor_id in sorted(org.vendor_ids - listed):
        findings.append(f"hub vendor-inventory.md: {vendor_id} is in vendors.csv but not in the inventory")
    for vendor_id in sorted(listed - org.vendor_ids):
        findings.append(f"hub vendor-inventory.md: {vendor_id} is not in vendors.csv")

    # Vendor contacts (guest accounts): a real vendor, and time-bound once access is granted
    for c in org.contacts:
        if c["vendor_id"] not in org.vendor_ids:
            findings.append(f"vendor-contacts.csv: {c['contact_id']} cites {c['vendor_id']}, not in vendors.csv")
        if c["status"] in ("Approved", "Active") and not (c["access_start"] and c["access_end"]):
            findings.append(f"vendor-contacts.csv: {c['contact_id']} is {c['status']} without access_start and access_end")

    for repo, root in [("hub", hub), ("IAM", iam), ("VRA", vra)]:
        if not root:
            continue
        for path in tracked_files(root):
            if path.suffix not in {".md", ".csv"} or path.name == "CLAUDE.md":
                continue
            for vendor_id in set(re.findall(r"\bV-\d{3}\b", read_text(path))):
                if vendor_id not in org.vendor_ids:
                    findings.append(f"{repo} {rel(path, root)}: {vendor_id} is not in vendors.csv")
    return findings


def access_level(value):
    """Normalise access levels from different exports to admin / standard / cashier."""
    value = value.lower()
    if "admin" in value:
        return "admin"
    if "cashier" in value:
        return "cashier"
    if "user" in value or "standard" in value:
        return "standard"
    return value


def check_evidence_agrees(hub, iam, org):
    """Hub evidence and the IAM access matrix must agree on the same person and system."""
    findings = []
    matrix = {}
    for row in read_csv(Path(iam) / "evidence" / "user-access-matrix.csv"):
        matrix[(row["User_Name"], row["System"])] = row
    access = Path(hub) / "07-evidence-pack" / "artifacts" / "access"

    def person_for(account):
        person = org.by_upn.get(account.strip().lower())
        return person["display_name"] if person else None

    for i, row in enumerate(read_csv(access / "mfa-status.csv"), start=2):
        name = person_for(row["User"])
        theirs = matrix.get((name, row["System"]))
        if name and theirs and theirs["MFA_Enabled"] != row["MFA Enabled"]:
            findings.append(f"MFA for {name} on {row['System']}: hub mfa-status.csv:{i} says "
                            f"'{row['MFA Enabled']}', IAM matrix says '{theirs['MFA_Enabled']}'")
    for i, row in enumerate(read_csv(access / "user-access-review.csv"), start=2):
        name = person_for(row["Username"])
        theirs = matrix.get((name, row["System"]))
        if name and theirs and access_level(row["Role"]) != access_level(theirs["Access_Level"]):
            findings.append(f"Access for {name} on {row['System']}: hub user-access-review.csv:{i} says "
                            f"'{row['Role']}', IAM matrix says '{theirs['Access_Level']}'")
    return findings


def check_ids(hub):
    findings = []
    hub = Path(hub)
    poam = table_with(hub / "07-evidence-pack" / "poam" / "poam.md", "POA&M ID")
    risks = table_with(hub / "02-risk-management" / "risk-register.md", "Risk ID")
    evidence = table_with(hub / "07-evidence-pack" / "evidence-matrix.md", "Evidence ID")
    matrix = table_with(hub / "03-controls" / "control-matrix.md", "Control ID")

    for label, rows, column in [("POA&M", poam, "POA&M ID"), ("risk register", risks, "Risk ID"),
                                ("evidence matrix", evidence, "Evidence ID")]:
        seen = set()
        for row in rows:
            item = row[column]
            if item in seen:
                findings.append(f"{label}: duplicate ID {item}")
            seen.add(item)

    poam_ids = {r["POA&M ID"] for r in poam}
    risk_ids = {r["Risk ID"] for r in risks}
    evidence_ids = {r["Evidence ID"] for r in evidence}
    for row in matrix:
        control = row["Control ID"]
        if row.get("Risk ID") not in risk_ids:
            findings.append(f"control matrix: {control} cites {row.get('Risk ID')}, not in the risk register")
        if row.get("Evidence ID") not in evidence_ids:
            findings.append(f"control matrix: {control} cites {row.get('Evidence ID')}, not in the evidence matrix")
        if row.get("POA&M ID", "-") not in poam_ids | {"-", ""}:
            findings.append(f"control matrix: {control} cites {row['POA&M ID']}, not in the POA&M")
    return findings


def check_links(hub, iam, vra):
    findings = []
    for repo, root in [("IAM", iam), ("VRA", vra)]:
        if root and HUB_URL not in read_text(Path(root) / "README.md"):
            findings.append(f"{repo} README.md does not link the program hub")
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    for path in tracked_files(hub):
        if path.suffix != ".md":
            continue
        for target in link.findall(strip_code(read_text(path))):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            if not resolved.exists():
                findings.append(f"hub {rel(path, hub)}: broken link '{target}'")
    return findings


def check_controls(hub):
    findings = []
    hub = Path(hub)
    matrix = {r["Control ID"]: r for r in table_with(hub / "03-controls" / "control-matrix.md", "Control ID")}
    crosswalk = {r["NIST Control"]: r for r in table_with(hub / "03-controls" / "nist-pci-crosswalk.md", "NIST Control")}
    for control in sorted(set(matrix) - set(crosswalk)):
        findings.append(f"{control} is in the control matrix but not the crosswalk")
    for control in sorted(set(crosswalk) - set(matrix)):
        findings.append(f"{control} is in the crosswalk but not the control matrix")
    for control in sorted(set(matrix) & set(crosswalk)):
        a = matrix[control].get("Implementation Status")
        b = crosswalk[control].get("Impl. Status")
        if a != b:
            findings.append(f"{control}: control matrix says '{a}', crosswalk says '{b}'")
    claim = re.search(r"(\d+) controls across (\d+) families", read_text(hub / "README.md"))
    if claim:
        families = {c.split("-")[0] for c in matrix}
        if int(claim.group(1)) != len(matrix) or int(claim.group(2)) != len(families):
            findings.append(f"README claims {claim.group(1)} controls across {claim.group(2)} families; "
                            f"the matrix has {len(matrix)} across {len(families)}")
    return findings


def check_counts(hub, org):
    findings = []
    profile = read_text(Path(hub) / "00-company-profile" / "company_profile.md")
    expected = org.store_headcount()
    claim = re.search(r"approximately (\d+) employees|(\d+) (?:active )?store staff", profile)
    if not claim:
        findings.append("company_profile.md states no headcount")
    elif int(claim.group(1) or claim.group(2)) != expected:
        findings.append(f"company_profile.md says {claim.group(1) or claim.group(2)}; "
                        f"people.csv has {expected} active store staff")
    return findings


def without_revision_history(text):
    """Drop '## Revision History' sections: they record what was removed, which is allowed."""
    return re.sub(r"^#+ Revision History.*?(?=^## |\Z)", "", text, flags=re.M | re.S)


def check_forbidden(repos):
    findings = []
    for repo, root in repos:
        for path in tracked_files(root):
            if path.suffix not in SCANNED_SUFFIXES or path.name == "CLAUDE.md":
                continue
            # The checker's own code and saved runs necessarily name what they look for
            if rel(path, root).startswith(("tools/", "07-evidence-pack/artifacts/consistency/")):
                continue
            text = without_revision_history(read_text(path))
            where = f"{repo} {rel(path, root)}"
            if re.search(r"\bstripe\b", text, re.I):
                findings.append(f"{where}: mentions Stripe before CR-002")
            if path.suffix == ".md" and re.search(r"\bTODO\b", text):
                findings.append(f"{where}: contains TODO")
            # Unfilled template placeholders (templates and examples are meant to have them)
            is_template = "template" in path.name or "examples" in path.parts
            if not is_template and re.search(r"YYYY-MM-DD|\[(?:Name|Date|TBD)\b[^\]]*\]", text):
                findings.append(f"{where}: unfilled template placeholder")
            for label, pattern in PERSONAL_DATA_PATTERNS.items():
                if pattern.search(text):
                    findings.append(f"{where}: {label}")
    return findings


def check_secrets(repos):
    findings = []
    for repo, root in repos:
        for path in tracked_files(root):
            where = f"{repo} {rel(path, root)}"
            if path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example"):
                findings.append(f"{where}: environment file is tracked by git")
                continue
            if path.suffix not in SCANNED_SUFFIXES or not path.exists():
                continue
            # The all-zeros GUID is the placeholder used in .env.example
            text = read_text(path).replace("00000000-0000-0000-0000-000000000000", "")
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(text):
                    findings.append(f"{where}: {label}")
    return findings


# ---------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--hub", default=".", help="path to grc-paper-project-coffee-shop")
    parser.add_argument("--iam", help="path to IAM-Access-Review-Lab")
    parser.add_argument("--vra", help="path to Vendor-Risk-Assessment-Lab")
    args = parser.parse_args()

    hub = Path(args.hub).resolve()
    iam = Path(args.iam).resolve() if args.iam else None
    vra = Path(args.vra).resolve() if args.vra else None
    repos = [(name, root) for name, root in [("hub", hub), ("IAM", iam), ("VRA", vra)] if root]
    org = Org(hub)
    cross = "needs --iam and --vra" if not (iam and vra) else None

    print(f"Burn and Churn program consistency check ({', '.join(name for name, _ in repos)})")
    print()
    report = Report()
    report.add(1, "People match people.csv", check_people(hub, iam, org))
    report.add(2, "Systems and vendors match systems.csv and vendors.csv", check_systems_and_vendors(hub, iam, vra, org))
    report.add(3, "IDs are unique and resolve", check_ids(hub))
    report.add(4, "Links resolve and companions link the hub", check_links(hub, iam, vra))
    report.add(5, "Control matrix, crosswalk and README agree", check_controls(hub))
    report.add(6, "Headcount matches people.csv", check_counts(hub, org))
    report.add(7, "No forbidden terms or personal data", check_forbidden(repos))
    report.add(8, "No secrets or tenant identifiers committed", check_secrets(repos))
    report.add(9, "Hub evidence agrees with the IAM access matrix",
               check_evidence_agrees(hub, iam, org) if iam else [], skipped="needs --iam" if not iam else None)
    if cross:
        print(f"Note: cross-repository parts of checks 1, 2, 4, 7 and 8 were skipped ({cross}).")
        print()
    return 1 if report.print() else 0


if __name__ == "__main__":
    sys.exit(main())
