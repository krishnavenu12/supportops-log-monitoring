from app.database import fetch_logs

# Returns only the critical alerts from logs
def get_critical_alerts():
    all_logs = fetch_logs()
    critical_logs = [log for log in all_logs if log["severity"] == "CRITICAL"]
    return critical_logs
