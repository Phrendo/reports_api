import pytest
from datetime import date
from app.services.em_service import EmService
from app.repositories.em_repository import SqlEmRepository

def test_service_integration(sample_date):
    repo = SqlEmRepository()
    service = EmService(repo)
    records = service.get_em_envelope(date.fromisoformat(sample_date))
    assert isinstance(records, list)
