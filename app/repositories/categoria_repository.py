from app.models.categoria import Categoria
from app.repositories.repository import BaseRepository

class CategoriaRepository(BaseRepository[Categoria]):
    def __init__(self, session):
        super().__init__(session, Categoria)

  