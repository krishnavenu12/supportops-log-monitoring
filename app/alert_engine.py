from app.models import LogEntry
from app.database import logs, alerts

SEVERITY_THRESHOLD = {"ERROR", "CRITICAL"}

def process_log(entry: LogEntry) -> bool:
    logs.append(entry)
    if entry.level.upper() in SEVERITY_THRESHOLD:
        alerts.append(entry)
        print(f"[ALERT] {entry.level} from {entry.service}: {entry.message}")
        return True
    return False

def get_critical_alerts():
    return [alert for alert in alerts if alert.level.upper() == "CRITICAL"]
