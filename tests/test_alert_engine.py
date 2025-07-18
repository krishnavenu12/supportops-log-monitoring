from app.alert_engine import process_log
from app.database import clear_alerts, get_all_alerts

def test_alert_processing():
    clear_alerts()
    log = {
        "timestamp": "2025-07-18T10:00:00Z",
        "severity": "CRITICAL",
        "service": "auth",
        "message": "Critical failure"
    }
    assert process_log(log) == True
    alerts = get_all_alerts()
    assert any(a["severity"] == "CRITICAL" for a in alerts)
