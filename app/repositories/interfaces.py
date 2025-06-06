from datetime import date
from typing import List
from app.schemas.em_models import EmRecord

class IReportRepository:
    def get_em_envelope(self, report_date: date, report_time: time) -> List[EmRecord]:
        raise NotImplementedError
