#!/usr/bin/env python3
"""Due-date monitor for the Burn and Churn Coffee security program.

Reads the program's own records and reports what is overdue or coming up. It never writes
or changes a record: it only reports what the records show, so a missed date stays visible
until a person does the work and records it.

It reads:
  - dated remediation targets: hub POA&M ("by YYYY-MM-DD"), the IAM remediation tracker,
    and the Vendor lab remediation trackers
  - dated, unticked items in the deferred-corrections register (CLAUDE.md section 13)
  - recurring activities, from the date they were last recorded (POA&M review log,
    POS inspections, update windows, access reviews, training, firewall review)

Usage (from the hub root, with the labs cloned alongside it):
    python tools/due_dates.py --hub . --iam ../IAM-Access-Review-Lab --vra ../Vendor-Risk-Assessment-Lab
    python tools/due_dates.py --hub . --today 2026-12-15        # report as of another date

Prints a Markdown report. Exit code is always 0: being behind is a finding, not a failure.
Standard library only.
"""
import argparse
import calendar
import csv
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ISO = re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b")
MONTH_YEAR = re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December) (20\d\d)\b")
CLOSED = ("closed", "done", "complete", "superseded")
LEADING_DATE = re.compile(r"^(?:By |Within .*? by )?(?:20\d\d-\d\d-\d\d|[A-Z][a-z]+ 20\d\d)\b")


def to_date(match):
    return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))


def first_due(text):
    """The first deadline in a piece of text: an ISO date, or the last day of 'Month YYYY'."""
    iso = ISO.search(text)
    month = MONTH_YEAR.search(text)
    if iso and (not month or iso.start() < month.start()):
        return to_date(iso)
    if month:
        m = list(calendar.month_name).index(month.group(1))
        y = int(month.group(2))
        return date(y, m, calendar.monthrange(y, m)[1])
    return None


def md_rows(path, required):
    """Rows (header -> cell) of every Markdown table in a file whose header has the required columns."""
    rows, header = [], None
    for line in Path(path).read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not (line.startswith("|") and line.endswith("|")):
            header = None
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if header is None:
            header = cells
        elif set("".join(cells)) <= set("-: "):
            continue
        elif all(col in header for col in required):
            rows.append(dict(zip(header, cells)))
    return rows


def section(text, start, end):
    s = text.find(start)
    if s == -1:
        return ""
    e = text.find(end, s + len(start))
    return text[s:e if e != -1 else len(text)]


# ---------------------------------------------------------------- deadlines

def poam_deadlines(hub):
    path = hub / "07-evidence-pack/poam/poam.md"
    for r in md_rows(path, ("POA&M ID", "Status")):
        if r["Status"].lower().startswith(CLOSED):
            continue
        for d in re.findall(r"\bby (20\d\d-\d\d-\d\d)", r["Planned Remediation"]):
            yield f"{r['POA&M ID']} ({r['Control ID']})", "hub POA&M", date.fromisoformat(d)


def register_deadlines(hub):
    text = section((hub / "CLAUDE.md").read_text(encoding="utf-8"), "## 13. Deferred corrections register", "\n## 14.")
    trigger = ""
    for line in text.splitlines():
        if line.startswith("### "):
            trigger = line[4:].split(".")[0]
        elif line.startswith("- [ ]") and trigger != "T10":
            # Only items that start with their deadline ("By 2026-11-30:", "November 2026:");
            # dates mentioned in passing are not deadlines
            summary = re.sub(r"[*`]", "", line[6:]).strip()
            due = first_due(summary) if LEADING_DATE.match(summary) else None
            if due:
                yield f"{trigger}: {summary[:90]}{'…' if len(summary) > 90 else ''}", "CLAUDE.md register", due


def iam_deadlines(iam):
    # One tracker per review under reviews/<period>/ (P4), or the original top-level tracker.
    # Global IDs follow identifiers.md: IAM:F-### for Q1 2026, IAM-Q4:F-### for later reviews.
    trackers = sorted(iam.glob("reviews/*/remediation/remediation-tracker.csv"))
    if not trackers and (iam / "remediation/remediation-tracker.csv").exists():
        trackers = [iam / "remediation/remediation-tracker.csv"]
    for path in trackers:
        period = path.parts[-3] if "reviews" in path.parts else "2026-Q1"
        prefix = "IAM" if period == "2026-Q1" else f"IAM-{period.split('-')[-1]}"
        with open(path, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                if r["Status"].lower().startswith(CLOSED) or not ISO.search(r["Target_Date"]):
                    continue
                yield f"{prefix}:{r['Finding_ID']} {r['Issue']}", f"IAM tracker ({period})", date.fromisoformat(r["Target_Date"])


def vra_deadlines(vra):
    for path in sorted(vra.glob("assessments/*/remediation/remediation-tracker.md")):
        vendor = path.parts[-3].split("-")[1]  # assessments/V-001-toast/... -> 001
        for r in md_rows(path, ("Finding ID", "Target", "Status")):
            due = first_due(r["Target"])
            if due and not r["Status"].lower().startswith(CLOSED):
                yield f"VRA-V{vendor}:{r['Finding ID']} {r.get('Remediation Action', '')[:60]}", "Vendor lab tracker", due


def exception_expiries(hub):
    path = hub / "02-risk-management/risk-exceptions.md"
    if not path.exists():
        return
    for r in md_rows(path, ("ID", "Expires", "Status")):
        if r["Status"].lower().startswith(CLOSED) or not ISO.search(r["Expires"]):
            continue
        yield f"{r['ID']} expires: {r['Requirement not met'][:70]}", "exception register", to_date(ISO.search(r["Expires"]))


# ---------------------------------------------------------------- recurring

def latest(dates):
    dates = [d for d in dates if d]
    return max(dates) if dates else None


def csv_dates(path, column, where=None):
    if not path.exists():
        return []
    with open(path, encoding="utf-8-sig", newline="") as f:
        return [date.fromisoformat(r[column]) for r in csv.DictReader(f)
                if ISO.fullmatch(r[column] or "") and (where is None or where(r))]


def recurring(hub, iam):
    """(activity, source, last recorded, interval in days, first due if never recorded)."""
    poam = hub / "07-evidence-pack/poam/poam.md"
    review_log = section(poam.read_text(encoding="utf-8"), "## POA&M Review Log", "\n## ")
    yield ("POA&M review (CA-5)", "POA&M review log",
           latest(to_date(m) for m in ISO.finditer(review_log)), 31, None)
    yield ("POS device inspection (PR-006)", "physical inspection records",
           latest(csv_dates(hub / "07-evidence-pack/artifacts/physical/physical-inspection-checklist.csv", "date")), 31, None)
    yield ("Monthly update window (PR-002)", "maintenance log",
           latest(csv_dates(hub / "01-asset-inventory/maintenance-log.csv", "date", lambda r: r["activity"] == "Update")),
           31, date(2026, 12, 31))
    yield ("Equipment register check (PR-010)", "maintenance log",
           latest(csv_dates(hub / "01-asset-inventory/maintenance-log.csv", "date", lambda r: r["activity"] == "Register check")),
           92, date(2027, 2, 15))
    if iam:
        history = md_rows(iam / "README.md", ("Review", "Date"))
        yield ("Quarterly access review (PR-003)", "IAM review history",
               latest(to_date(m) for r in history for m in ISO.finditer(r["Date"]) if "planned" not in r["Date"].lower()), 92, None)
    yield ("Security awareness training (PR-007)", "training log",
           latest(csv_dates(hub / "07-evidence-pack/artifacts/training/security-training-log.csv", "date")), 365, None)
    backup_log = hub / "07-evidence-pack/artifacts/backup/backup-log.csv"
    yield ("Offline backup copy (PR-012)", "backup log",
           latest(csv_dates(backup_log, "date", lambda r: r["activity"] == "Backup")), 31, date(2026, 12, 31))
    yield ("Restore test (PR-012)", "backup log",
           latest(csv_dates(backup_log, "date", lambda r: r["activity"] == "Restore test")), 92, date(2027, 2, 28))
    yield ("Tabletop exercise (P-003 §6.7, PR-005 §8)", "tabletop log",
           latest(csv_dates(hub / "07-evidence-pack/artifacts/monitoring/tabletop-log.csv", "date")), 365, date(2026, 12, 31))
    yield ("Records retention review (P-010 §4)", "disposal log",
           latest(csv_dates(hub / "07-evidence-pack/artifacts/assets/disposal-log.csv", "date", lambda r: r["item"] == "Yearly review")), 365, date(2027, 1, 31))
    yield ("Firewall rule review (P-005 §6)", "no record kept yet", None, 182, date(2027, 4, 30))


# ---------------------------------------------------------------- report

def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--hub", default=".")
    parser.add_argument("--iam")
    parser.add_argument("--vra")
    parser.add_argument("--today", help="report as of this date (YYYY-MM-DD); default is today")
    parser.add_argument("--window", type=int, default=30, help="days ahead to list as coming up (default 30)")
    parser.add_argument("--output", help="also write the report to this file")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    lines = []
    emit = lines.append

    hub = Path(args.hub).resolve()
    iam = Path(args.iam).resolve() if args.iam else None
    vra = Path(args.vra).resolve() if args.vra else None
    today = date.fromisoformat(args.today) if args.today else date.today()
    horizon = today + timedelta(days=args.window)

    deadlines = list(poam_deadlines(hub)) + list(register_deadlines(hub)) + list(exception_expiries(hub))
    if iam:
        deadlines += list(iam_deadlines(iam))
    if vra:
        deadlines += list(vra_deadlines(vra))
    deadlines = sorted(set(deadlines), key=lambda d: (d[2], d[0]))
    overdue = [d for d in deadlines if d[2] < today]
    upcoming = [d for d in deadlines if today <= d[2] <= horizon]

    emit(f"# Program monitor: {today.isoformat()}")
    emit("")
    emit("Read from the program's records; nothing here is generated evidence. "
          "A missed date stays listed until the work is done and recorded.")
    if not (iam and vra):
        emit("")
        emit("_Lab trackers not read (run with --iam and --vra for the full picture)._")

    emit("")
    emit(f"## Overdue ({len(overdue)})")
    emit("")
    if overdue:
        emit("| Item | Source | Due | Days overdue |")
        emit("|---|---|---|---|")
        for item, source, due in overdue:
            emit(f"| {item} | {source} | {due} | {(today - due).days} |")
    else:
        emit("Nothing overdue.")

    emit("")
    emit(f"## Due in the next {args.window} days ({len(upcoming)})")
    emit("")
    if upcoming:
        emit("| Item | Source | Due |")
        emit("|---|---|---|")
        for item, source, due in upcoming:
            emit(f"| {item} | {source} | {due} |")
    else:
        emit("Nothing due.")

    emit("")
    emit("## Recurring activities")
    emit("")
    emit("| Activity | Last recorded | Next due | Status | Source |")
    emit("|---|---|---|---|---|")
    for activity, source, last, interval, first in recurring(hub, iam):
        due = last + timedelta(days=interval) if last else first
        if due is None:
            status = "**Never recorded**"
        elif due < today:
            status = f"**Overdue** ({(today - due).days} days)"
        elif due <= horizon:
            status = "Due soon"
        else:
            status = "On track"
        emit(f"| {activity} | {last or 'never'} | {due or 'now'} | {status} | {source} |")
    report = "\n".join(lines) + "\n"
    sys.stdout.write(report)
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
