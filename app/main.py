from fastapi import FastAPI
from pydantic import BaseModel
from app import database, alert_engine

app = FastAPI()
database.init_db()

class Log(BaseModel):
    timestamp: str
    severity: str
    service: str
    message: str

@app.post("/log")
def receive_log(log: Log):
    log_data = log.dict()
    alert_engine.process_log(log_data)
    database.insert_log(log_data)
    return {"status": "received"}

@app.get("/alerts")
def get_alerts():
    return alert_engine.get_alerts()

@app.get("/logs")
def get_logs():
    return database.fetch_all_logs()
