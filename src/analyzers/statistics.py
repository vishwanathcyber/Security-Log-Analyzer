"""
Statistics Module
"""

def generate_statistics(events):

    stats = {

        "total_events": len(events),

        "failed_logins": 0,

        "successful_logins": 0

    }

    for event in events:

        if "Failed password" in event:

            stats["failed_logins"] += 1

        elif "Accepted password" in event:

            stats["successful_logins"] += 1

    return stats
