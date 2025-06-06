import pytest
from datetime import date
from app.repositories.em_repository import SqlEmRepository

def test_get_em_envelope_returns_list(sample_date):
    repo = SqlEmRepository()
    records = repo.get_em_envelope(date.fromisoformat(sample_date))
    assert isinstance(records, list)
