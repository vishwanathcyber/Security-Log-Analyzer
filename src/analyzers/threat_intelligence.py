"""
Threat Intelligence Module
"""

def classify_ip_reputation(ip):

    suspicious = [

        "192.168.1.20",

        "10.0.0.5"

    ]

    if ip in suspicious:

        return "Suspicious"

    return "Unknown"
