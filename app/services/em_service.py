from datetime import date
from typing import List
from app.repositories.interfaces import IReportRepository
from app.schemas.em_models import EmRecord

class EmService:
    def __init__(self, repository: IReportRepository):
        self.repository = repository

    def get_em_envelope(self, report_date: date, report_time: time) -> List[EmRecord]:
        return self.repository.get_em_envelope(report_date, report_time)
