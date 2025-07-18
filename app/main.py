from fastapi import FastAPI
from app.models import LogEntry
from app.alert_engine import process_log, get_critical_alerts

app = FastAPI(
    title="SupportOps Log Monitoring System",
    description="Simulates a backend system for real-time log ingestion, classification, and alerting",
    version="1.0.0"
)

# 🔸 POST /log — Submit a log entry
@app.post("/log", summary="Submit a log entry")
def receive_log(entry: LogEntry):
    """
    Receives a log entry and triggers an alert if severity is ERROR or CRITICAL.
    """
    alert_triggered = process_log(entry)
    return {
        "message": "Log received",
        "alert_triggered": alert_triggered
    }

# 🔹 GET /alerts — View critical alerts
@app.get("/alerts", summary="Get all active critical alerts")
def show_critical_alerts():
    """
    Returns a list of log entries classified as CRITICAL alerts.
    """
    return get_critical_alerts()
