"""
Security Log Analyzer

Main entry point of the application.
"""

from parsers.auth_parser import parse_auth_log
from analyzers.failed_login import detect_failed_logins

def main():
    print("=" * 50)
    print("Security Log Analyzer")
    print("=" * 50)

    log_file = "logs/auth.log"

    events = parse_auth_log(log_file)

    detect_failed_logins(events)

if name == "main":
    main()
