import csv
from datetime import datetime
from pathlib import Path

# Anchor the path to this script's location so it runs from any directory
FILE_PATH = Path(__file__).resolve().parent.parent / "access" / "user-access-review.csv"

# Accounts with no login activity for longer than this, relative to their
# review date, are flagged as inactive regardless of review status.
#
# This number is an illustrative assumption, not derived from a real
# company's access-review cadence -- this project has no live organization
# to calibrate against. A real deployment should set this from the org's
# actual quarterly-review policy (see PR-003-quarterly-access-review.md)
# rather than reusing this default as-is.
INACTIVITY_THRESHOLD_DAYS = 30

def review_user_access():
    flagged_accounts = []

    try:
        with open(FILE_PATH, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                username = row["Username"]
                system = row["System"]
                role = row["Role"]
                access_level = row["Access Level"]
                last_login = row["Last Login"]
                review_status = row["Review Status"]
                reviewer = row["Reviewer"]
                review_date = row["Review Date"]

                reasons = []

                if review_status.strip().lower() != "approved":
                    reasons.append(f"Review status is '{review_status}'")

                try:
                    login_date = datetime.strptime(last_login, "%Y-%m-%d")
                    reviewed_date = datetime.strptime(review_date, "%Y-%m-%d")
                    days_inactive = (reviewed_date - login_date).days
                    if days_inactive > INACTIVITY_THRESHOLD_DAYS:
                        reasons.append(
                            f"No login activity for {days_inactive} days prior to review"
                        )
                except ValueError:
                    reasons.append("Invalid or missing Last Login / Review Date value")

                if reasons:
                    flagged_accounts.append({
                        "Username": username,
                        "System": system,
                        "Role": role,
                        "Access Level": access_level,
                        "Last Login": last_login,
                        "Review Status": review_status,
                        "Reviewer": reviewer,
                        "Review Date": review_date,
                        "Reasons": "; ".join(reasons)
                    })

    except FileNotFoundError:
        print(f"[ERROR] File not found: {FILE_PATH}")
        return

    print("\n=== User Access Review Report ===\n")

    if not flagged_accounts:
        print("All user accounts are reviewed and active.")
    else:
        for acct in flagged_accounts:
            print(f"User: {acct['Username']}")
            print(f"System: {acct['System']}")
            print(f"Role: {acct['Role']}")
            print(f"Access Level: {acct['Access Level']}")
            print(f"Last Login: {acct['Last Login']}")
            print(f"Review Status: {acct['Review Status']}")
            print(f"Reviewer: {acct['Reviewer']}")
            print(f"Review Date: {acct['Review Date']}")
            print(f"Flag Reason(s): {acct['Reasons']}")
            print("-" * 40)

    print("\nReview Complete.\n")

if __name__ == "__main__":
    review_user_access()
