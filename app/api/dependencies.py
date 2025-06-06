from app.repositories.em_repository import SqlEmRepository
from app.services.em_service import EmService

def get_repository():
    return SqlEmRepository()

def get_service(repo: SqlEmRepository = get_repository()):
    return EmService(repo)
