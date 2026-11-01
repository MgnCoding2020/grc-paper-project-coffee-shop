"""Redact a raw tenant export so it can be committed as evidence.

Reads a raw export (CSV, JSON or text) from the git-ignored _raw/ folder and writes a copy that
uses the fictional domain only:

  - the real tenant domain (ENTRA_TENANT_DOMAIN in .env) becomes BC_DOC_DOMAIN
  - every real email address listed in .env (any key containing EMAIL) becomes a readable
    stand-in at example.com (VENDOR_GUEST_EMAIL_VC001 -> vendor.guest.vc001@example.com)
  - the tenant ID and any other GUID becomes <guid>
  - IPv4 and IPv6 addresses become <ip>
  - access tokens (JWT-shaped) become <token>
  - any remaining email outside the fictional domain or example.com becomes <email>

It then rescans the output and refuses to write it if anything tenant-shaped is left.

Usage (from the hub root):
    python tools/tenant/redact_export.py _raw/signins.csv 07-evidence-pack/artifacts/tenant/2026-11-15-signins.csv

Standard library only. Values come from .env at runtime and are never printed.
"""
import argparse
import re
import sys
from pathlib import Path

GUID = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")
IPV4 = re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])")
# Full form (eight groups) or compressed form (with "::"); a bare time like 09:01:02 is neither
IPV6 = re.compile(r"(?<![0-9A-Fa-f:])(?:(?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:)*[0-9A-Fa-f]{0,4}::(?:[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4})*)?)(?![0-9A-Fa-f:])")
JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")
ONMICROSOFT = re.compile(r"[A-Za-z0-9.-]+\.onmicrosoft\.com", re.I)


def read_env(path):
    values = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"')
    for key in ("ENTRA_TENANT_DOMAIN", "BC_DOC_DOMAIN"):
        if not values.get(key):
            sys.exit(f"{key} is not set in {path}")
    return values


def redact(text, env):
    doc = env["BC_DOC_DOMAIN"]
    allowed = {doc.lower(), "example.com"}
    # Real addresses from .env first, so they map to a readable fictional stand-in
    for key, value in env.items():
        if "EMAIL" in key and "@" in value:
            stand_in = re.sub(r"_?email_?", ".", key.lower()).strip(".").replace("_", ".") + "@example.com"
            text = re.sub(re.escape(value), stand_in, text, flags=re.I)
    text = re.sub(re.escape(env["ENTRA_TENANT_DOMAIN"]), doc, text, flags=re.I)
    text = ONMICROSOFT.sub(doc, text)
    text = JWT.sub("<token>", text)
    text = GUID.sub("<guid>", text)
    text = IPV4.sub("<ip>", text)
    text = IPV6.sub("<ip>", text)
    return EMAIL.sub(lambda m: m.group(0) if m.group(1).lower() in allowed else "<email>", text)


def leftovers(text, env):
    problems = []
    secrets = [env["ENTRA_TENANT_DOMAIN"], env.get("ENTRA_TENANT_ID", "")]
    secrets += [v for k, v in env.items() if "EMAIL" in k]
    if any(s and s.lower() in text.lower() for s in secrets):
        problems.append("a value from .env")
    for label, pattern in (("GUID", GUID), ("IPv4", IPV4), ("IPv6", IPV6), ("token", JWT), ("onmicrosoft domain", ONMICROSOFT)):
        if pattern.search(text):
            problems.append(label)
    return problems


def main():
    parser = argparse.ArgumentParser(description="Redact a raw tenant export for committing as evidence.")
    parser.add_argument("source", help="raw export, normally under _raw/")
    parser.add_argument("output", help="redacted copy, normally under 07-evidence-pack/artifacts/")
    parser.add_argument("--env", default=".env", help="path to .env (default: .env in the current folder)")
    args = parser.parse_args()

    env = read_env(args.env)
    text = Path(args.source).read_text(encoding="utf-8-sig")
    clean = redact(text, env)
    problems = leftovers(clean, env)
    if problems:
        sys.exit(f"Not written: the output still contains {', '.join(problems)}. Check the source by hand.")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(clean, encoding="utf-8")
    print(f"Redacted {args.source} -> {args.output}")


if __name__ == "__main__":
    main()
