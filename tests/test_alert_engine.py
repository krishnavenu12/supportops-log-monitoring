from app.alert_engine import process_log, get_alerts

def test_alert_processing():
    # Clear previous alerts (for clean testing)
    alerts = get_alerts()
    alerts.clear()

    sample_log = {
        "timestamp": "2025-07-18T10:30:00Z",
        "severity": "ERROR",
        "service": "auth-service",
        "message": "Login failed for user"
    }

    process_log(sample_log)

    assert len(get_alerts()) == 1
    assert get_alerts()[0]["severity"] == "ERROR"
    assert get_alerts()[0]["service"] == "auth-service"
