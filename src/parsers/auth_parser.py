"""
Authentication Log Parser
"""

def parse_auth_log(log_path):
    print(f"Reading log file: {log_path}")

    events = []

    try:
        with open(log_path, "r") as file:
            for line in file:
                events.append(line.strip())

    except FileNotFoundError:
        print("Log file not found.")

    return events
