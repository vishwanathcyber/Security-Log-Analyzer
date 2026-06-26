"""
Severity Classification
"""

def classify_severity(failed_attempts):

    if failed_attempts < 3:
        return "LOW"

    elif failed_attempts < 6:
        return "MEDIUM"

    elif failed_attempts < 10:
        return "HIGH"

    return "CRITICAL"
