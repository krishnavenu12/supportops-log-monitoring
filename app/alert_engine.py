# app/alert_engine.py

def is_critical(log):
    return log.get("severity", "").upper() == "CRITICAL"
