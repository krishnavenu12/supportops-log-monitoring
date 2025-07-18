alerts = []

def process_log(log):
    if log["severity"] in ["ERROR", "CRITICAL"]:
        alerts.append(log)

def get_alerts():
    return alerts
