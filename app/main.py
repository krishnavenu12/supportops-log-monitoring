from fastapi import FastAPI, HTTPException
from app.models import LogEntry
from app.database import init_db, fetch_logs, add_log, delete_log, update_log

app = FastAPI()

init_db()

@app.get("/logs")
def get_logs():
    rows = fetch_logs()
    logs = [
        {
            "id": row[0],
            "timestamp": row[1],
            "severity": row[2],
            "service": row[3],
            "message": row[4]
        } for row in rows
    ]
    return {"logs": logs}

@app.post("/logs")
def create_log(entry: LogEntry):
    add_log(entry.timestamp, entry.severity, entry.service, entry.message)
    return {"message": "Log added successfully"}

@app.put("/logs/{log_id}")
def edit_log(log_id: int, entry: LogEntry):
    update_log(log_id, entry.timestamp, entry.severity, entry.service, entry.message)
    return {"message": "Log updated"}

@app.delete("/logs/{log_id}")
def remove_log(log_id: int):
    delete_log(log_id)
    return {"message": "Log deleted"}
