from app.models.investimento import Investimento
from app.repositories.repository import BaseRepository

class InvestimentoRepository(BaseRepository[Investimento]):
    def __init__(self, session):
        super().__init__(session, Investimento)

    def atualizar(self,investimento):
        self.session.flush()

