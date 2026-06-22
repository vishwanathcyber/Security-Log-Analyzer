import re

print("=== Security Log Analyzer ===")

log_file = input("Enter log file name: ")

try:
    with open(log_file, "r") as file:
        logs = file.readlines()

    suspicious_count = 0
    ip_addresses = set()

    for line in logs:
        if re.search(r"failed|invalid|error", line, re.IGNORECASE):
            suspicious_count += 1
            print("[ALERT]", line.strip())

        ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
        for ip in ips:
            ip_addresses.add(ip)

    print("\nAnalysis Complete")
    print(f"Suspicious Entries Found: {suspicious_count}")

    print("\nIP Addresses Found:")
    for ip in ip_addresses:
        print("-", ip)

except FileNotFoundError:
    print("Log file not found.")
