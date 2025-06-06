from fastapi import APIRouter, Depends, HTTPException
from datetime import date, time
from app.services.em_service import EmService
from app.api.dependencies import get_service
from app.schemas.em_models import EmEnvelopeResponse

router = APIRouter()

@router.get("/{report_date}", response_model=EmEnvelopeResponse)

def read_em_envelope(report_date: date, report_time: time, service: EmService = Depends(get_service)):
    records = service.get_em_envelope(report_date, report_time)
    if not records:
        raise HTTPException(status_code=404, detail="No data for this date")
    return EmEnvelopeResponse(date=report_date, records=records)
