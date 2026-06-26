"""
Detection Rules Engine
"""

RULES = {

    "failed_login_threshold": 5,

    "bruteforce_threshold": 10,

    "suspicious_ip_threshold": 20

}

def load_rules():

    return RULES
