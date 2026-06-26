"""
Risk Score Engine
"""

def calculate_risk(failed_logins, brute_force_ips):

    score = 0

    score += failed_logins * 2

    score += brute_force_ips * 10

    if score < 20:
        level = "LOW"

    elif score < 40:
        level = "MEDIUM"

    elif score < 70:
        level = "HIGH"

    else:
        level = "CRITICAL"

    return score, level
