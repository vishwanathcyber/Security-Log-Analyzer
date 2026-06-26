"""
IOC Detection
"""

def detect_iocs(events):

    indicators = []

    for event in events:

        if "Failed password" in event:

            indicators.append(event)

    return indicators
