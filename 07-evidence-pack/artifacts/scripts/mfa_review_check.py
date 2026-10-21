import csv
from pathlib import Path

# Anchor the path to this script's location so it runs from any directory
FILE_PATH = Path(__file__).resolve().parent.parent / "access" / "mfa-status.csv"

def review_mfa_status():
    flagged_accounts = []

    try:
        with open(FILE_PATH, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                user = row["User"]
                system = row["System"]
                mfa_enabled = row["MFA Enabled"]
                mfa_method = row["MFA Method"]
                last_verified = row["Last Verified"]

                if mfa_enabled.strip().lower() != "yes":
                    flagged_accounts.append({
                        "User": user,
                        "System": system,
                        "MFA Enabled": mfa_enabled,
                        "MFA Method": mfa_method,
                        "Last Verified": last_verified,
                        "Reason": "MFA not enabled"
                    })
                elif last_verified.strip().upper() in ("N/A", ""):
                    flagged_accounts.append({
                        "User": user,
                        "System": system,
                        "MFA Enabled": mfa_enabled,
                        "MFA Method": mfa_method,
                        "Last Verified": last_verified,
                        "Reason": "MFA enabled but verification date missing"
                    })

    except FileNotFoundError:
        print(f"[ERROR] File not found: {FILE_PATH}")
        return

    print("\n=== MFA Enforcement Review Report ===\n")

    if not flagged_accounts:
        print("All accounts have MFA enabled and verified.")
    else:
        for acct in flagged_accounts:
            print(f"User: {acct['User']}")
            print(f"System: {acct['System']}")
            print(f"MFA Enabled: {acct['MFA Enabled']}")
            print(f"MFA Method: {acct['MFA Method']}")
            print(f"Last Verified: {acct['Last Verified']}")
            print(f"Reason: {acct['Reason']}")
            print("-" * 40)

    print("\nReview Complete.\n")

if __name__ == "__main__":
    review_mfa_status()
