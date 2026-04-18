import csv
from datetime import datetime

FILE_PATH = "../user-access-review.csv"
PRIVILEGED_ACCESS_LEVELS = {"Privileged", "Admin"}

def review_privileged_access():
    flagged_accounts = []

    try:
        with open(FILE_PATH, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                username = row["Username"]
                system = row["System"]
                role = row["Role"]
                access_level = row["Access Level"]
                review_status = row["Review Status"]
                reviewer = row["Reviewer"]
                review_date = row["Review Date"]

                if access_level in PRIVILEGED_ACCESS_LEVELS or role.lower() == "admin":
                    try:
                        datetime.strptime(review_date, "%Y-%m-%d")
                    except ValueError:
                        print(f"[ERROR] Invalid review date for user: {username}")
                        review_date = "Invalid Date"

                    if review_status.lower() != "approved":
                        flagged_accounts.append({
                            "Username": username,
                            "System": system,
                            "Role": role,
                            "Access Level": access_level,
                            "Review Status": review_status,
                            "Reviewer": reviewer,
                            "Review Date": review_date
                        })

    except FileNotFoundError:
        print(f"[ERROR] File not found: {FILE_PATH}")
        return

    print("\n=== Privileged Access Review Report ===\n")

    if not flagged_accounts:
        print("All privileged accounts are currently approved.")
    else:
        for acct in flagged_accounts:
            print(f"User: {acct['Username']}")
            print(f"System: {acct['System']}")
            print(f"Role: {acct['Role']}")
            print(f"Access Level: {acct['Access Level']}")
            print(f"Review Status: {acct['Review Status']}")
            print(f"Reviewer: {acct['Reviewer']}")
            print(f"Review Date: {acct['Review Date']}")
            print("-" * 40)

    print("\nReview Complete.\n")

if __name__ == "__main__":
    review_privileged_access()
