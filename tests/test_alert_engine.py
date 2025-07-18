from datetime import datetime
from app.models import LogEntry
from app.alert_engine import process_log

def test_alert_on_critical_log():
    log = LogEntry(timestamp=datetime.now(), service="API", level="CRITICAL", message="Service crashed")
    assert process_log(log) is True

def test_no_alert_on_info_log():
    log = LogEntry(timestamp=datetime.now(), service="Web", level="INFO", message="Routine check")
    assert process_log(log) is False
