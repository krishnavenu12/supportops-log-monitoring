from pydantic import BaseModel
from datetime import datetime

class LogEntry(BaseModel):
    id: int | None = None
    timestamp: datetime
    severity: str
    service: str
    message: str
