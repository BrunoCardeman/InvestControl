from app.models.atualizacao import Atualizacao
from app.repositories.repository import BaseRepository


class AtualizacaoRepository(BaseRepository[Atualizacao]):

    def __init__(self, session):
        super().__init__(session, Atualizacao)

    def listar_por_investimento(self, investimento_id):
        return self.session.query(Atualizacao).filter(Atualizacao.investimento_id == investimento_id).all()
    