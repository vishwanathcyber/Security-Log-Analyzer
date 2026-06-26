"""
Suspicious IP Detection
"""

from collections import Counter

def detect_suspicious_ips(events):

    print("\nChecking suspicious IP addresses...\n")

    ips = []

    for event in events:

        words = event.split()

        for word in words:

            if word.count(".") == 3:
                ips.append(word)

    counter = Counter(ips)

    print("Most Active IP Addresses:")

    for ip, count in counter.most_common(5):
        print(f"{ip} -> {count} events")
