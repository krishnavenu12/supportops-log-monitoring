from pydantic import BaseModel
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime
    service: str
    level: str  # INFO, WARN, ERROR, CRITICAL
    message: str
