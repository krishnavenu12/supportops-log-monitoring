from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import alert_engine, database

app = FastAPI()
database.init_db()  # initialize DB on startup

class Log(BaseModel):
    timestamp: str
    severity: str
    service: str
    message: str

@app.post("/log")
def receive_log(log: Log):
    log_data = log.dict()
    alert_engine.process_log(log_data)  # logic for alerts
    database.insert_log(log_data)  # save to DB
    return {"status": "received"}

@app.get("/alerts")
def get_alerts():
    return alert_engine.get_alerts()

@app.get("/logs")
def get_logs():
    return database.fetch_all_logs()
