# tests/test_alert_engine.py

from app.alert_engine import is_critical

def test_is_critical_true():
    log = {
        "timestamp": "2025-07-18T10:30:00Z",
        "severity": "CRITICAL",
        "service": "auth",
        "message": "Critical failure"
    }
    assert is_critical(log) == True

def test_is_critical_false():
    log = {
        "timestamp": "2025-07-18T10:35:00Z",
        "severity": "INFO",
        "service": "auth",
        "message": "Just info"
    }
    assert is_critical(log) == False

def test_is_critical_missing_field():
    log = {
        "timestamp": "2025-07-18T10:40:00Z",
        "service": "auth",
        "message": "No severity"
    }
    assert is_critical(log) == False

def test_is_critical_lowercase():
    log = {
        "severity": "critical"
    }
    assert is_critical(log) == True
