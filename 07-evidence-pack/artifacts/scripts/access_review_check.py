import csv
from datetime import datetime

FILE_PATH = "../user-access-review.csv"
INACTIVITY_THRESHOLD_DAYS = 30

def check_inactive_accounts():
    today = datetime.today()
    flagged_accounts = []

    try:
        with open(FILE_PATH, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                last_login_str = row["Last Login"]
                username = row["Username"]
                system = row["System"]
                access = row["Access Level"]
                review_status = row["Review Status"]

                try:
                    last_login = datetime.strptime(last_login_str, "%Y-%m-%d")
                    days_inactive = (today - last_login).days

                    if days_inactive > INACTIVITY_THRESHOLD_DAYS or review_status.lower() == "review required":
                        flagged_accounts.append({
                            "Username": username,
                            "System": system,
                            "Days Inactive": days_inactive,
                            "Access Level": access,
                            "Review Status": review_status
                        })

                except ValueError:
                    print(f"[ERROR] Invalid date format for user: {username}")

    except FileNotFoundError:
        print(f"[ERROR] File not found: {FILE_PATH}")
        return

    print("\n=== Access Review Report ===\n")

    if not flagged_accounts:
        print("No inactive or review-required accounts found.")
    else:
        for acct in flagged_accounts:
            print(f"User: {acct['Username']}")
            print(f"System: {acct['System']}")
            print(f"Days Inactive: {acct['Days Inactive']}")
            print(f"Access Level: {acct['Access Level']}")
            print(f"Review Status: {acct['Review Status']}")
            print("-" * 40)

    print("\nReview Complete.\n")

if __name__ == "__main__":
    check_inactive_accounts()
