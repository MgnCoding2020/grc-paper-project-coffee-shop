import re

FILE_PATH = "../incident-log.md"

def parse_incidents():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {FILE_PATH}")
        return

    incident_blocks = re.split(r"\n---\n", content)
    open_incidents = []

    for block in incident_blocks:
        if "## Incident" not in block:
            continue

        incident_id_match = re.search(r"## (Incident .+)", block)
        date_match = re.search(r"- Date:\s*(.+)", block)
        system_match = re.search(r"- System:\s*(.+)", block)
        user_match = re.search(r"- User:\s*(.+)", block)
        status_match = re.search(r"- Status:\s*\n\s*(.+)", block)

        incident_id = incident_id_match.group(1).strip() if incident_id_match else "Unknown Incident"
        date = date_match.group(1).strip() if date_match else "Unknown Date"
        system = system_match.group(1).strip() if system_match else "Unknown System"
        user = user_match.group(1).strip() if user_match else "Unknown User"
        status = status_match.group(1).strip() if status_match else "Unknown Status"

        if status.lower() != "resolved":
            open_incidents.append({
                "Incident": incident_id,
                "Date": date,
                "System": system,
                "User": user,
                "Status": status
            })

    print("\n=== Incident Log Review Report ===\n")

    if not open_incidents:
        print("No open incidents found.")
    else:
        for incident in open_incidents:
            print(f"Incident: {incident['Incident']}")
            print(f"Date: {incident['Date']}")
            print(f"System: {incident['System']}")
            print(f"User: {incident['User']}")
            print(f"Status: {incident['Status']}")
            print("-" * 40)

    print("\nReview Complete.\n")

if __name__ == "__main__":
    parse_incidents()
