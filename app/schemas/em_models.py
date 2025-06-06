from datetime import datetime, date
from pydantic import BaseModel

class EmRecord(BaseModel):
    T: datetime
    Mark: float
    LowerEM: float
    UpperEM: float
    LEM: float
    UEM: float
    V: int

class EmEnvelopeResponse(BaseModel):
    date: date
    records: list[EmRecord]
