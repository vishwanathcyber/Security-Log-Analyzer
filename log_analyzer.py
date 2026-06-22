import re

print("=== Security Log Analyzer ===")

log_file = input("Enter log file name: ")

try:
  with open(log_file, "r") as file:
    logs = file.readlines()

suspicious_count = 0

for line in logs:
  if re.searcg(r"failed|invalid|error", line,
               re.IGNORECASE):
                 suspicious_count += 1
                 print("[ALERT]", line.strip())

print("\nAnalysis Complete")
print(f"Suspicious Entries Found: {suspicious_count}")

except FileNotFoundError:
    print("Log file not found.")
