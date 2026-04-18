import csv
from datetime import datetime

FILE_PATH = "../mfa-status.csv"
VERIFICATION_STALENESS_DAYS = 30

def check_mfa_status():
    today = datetime.today()
    flagged_users = []

    try:
        with open(FILE_PATH, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                user = row["User"]
                system = row["System"]
                mfa_enabled = row["MFA Enabled"]
                mfa_method = row["MFA Method"]
                last_verified = row["Last Verified"]

                stale_verification = False

                if last_verified != "N/A":
                    try:
                        verified_date = datetime.strptime(last_verified, "%Y-%m-%d")
                        days_since_verification = (today - verified_date).days
                        stale_verification = days_since_verification > VERIFICATION_STALENESS_DAYS
                    except ValueError:
                        print(f"[ERROR] Invalid verification date for user: {user}")
                        stale_verification = True
                else:
                    days_since_verification = "N/A"
                    stale_verification = True

                if mfa_enabled.strip().lower() != "yes" or stale_verification:
                    flagged_users.append({
                        "User": user,
                        "System": system,
                        "MFA Enabled": mfa_enabled,
                        "MFA Method": mfa_method,
                        "Last Verified": last_verified,
                        "Days Since Verification": days_since_verification
                    })

    except FileNotFoundError:
        print(f"[ERROR] File not found: {FILE_PATH}")
        return

    print("\n=== MFA Review Report ===\n")

    if not flagged_users:
        print("All reviewed accounts have MFA enabled and recently verified.")
    else:
        for acct in flagged_users:
            print(f"User: {acct['User']}")
            print(f"System: {acct['System']}")
            print(f"MFA Enabled: {acct['MFA Enabled']}")
            print(f"MFA Method: {acct['MFA Method']}")
            print(f"Last Verified: {acct['Last Verified']}")
            print(f"Days Since Verification: {acct['Days Since Verification']}")
            print("-" * 40)

    print("\nReview Complete.\n")

if __name__ == "__main__":
    check_mfa_status()
