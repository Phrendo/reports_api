from app.repositories.em_repository import SqlEmRepository
from app.services.em_service import EmService

def get_service():
    repo = SqlEmRepository()
    return EmService(repo)
