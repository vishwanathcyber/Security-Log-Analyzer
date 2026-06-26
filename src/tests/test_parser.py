from parsers.auth_parser import parse_auth_log

def test_parser():

    events = parse_auth_log("logs/auth.log")

    assert len(events) > 0
