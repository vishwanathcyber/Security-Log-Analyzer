"""
Brute Force Attack Detection
"""

from collections import Counter

def detect_bruteforce(events):

    print("\nChecking for brute-force attacks...\n")

    failed_ips = []

    for event in events:

        if "Failed password" in event:

            words = event.split()

            for word in words:

                if word.count(".") == 3:
                    failed_ips.append(word)

    counter = Counter(failed_ips)

    for ip, count in counter.items():

        if count >= 5:
            print(f"[HIGH] Possible brute-force attack from {ip} ({count} failed attempts)")
