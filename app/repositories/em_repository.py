from datetime import date
from typing import List
import pandas as pd
from app.repositories.interfaces import IReportRepository
from app.schemas.em_models import EmRecord
from app.db.connection import get_db_connection

class SqlEmRepository(IReportRepository):
    def get_em_envelope(self, report_date: date) -> List[EmRecord]:
        sql = """SELECT T, Mark, LowerEM, UpperEM, LEM, UEM, V
FROM WEBOPT.REPORTS.TF_EM_BAND_VIOLATIONS(?)
"""
        conn = get_db_connection()
        df = pd.read_sql_query(sql, conn, params=[report_date])
        conn.close()
        records = [EmRecord(**row) for row in df.to_dict(orient="records")]
        return records
