"""
Failed Login Analyzer
"""

def detect_failed_logins(events):

    print("\nChecking for failed login attempts...\n")

    failed = 0

    for event in events:
        if "Failed password" in event:
            failed += 1

    print(f"Failed login attempts detected: {failed}")
