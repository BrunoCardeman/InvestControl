from app.models.atualizacao import Atualizacao

class AtualizacaoRepository:

    def __init__(self, session):
        self.session = session

    def listar_por_investimento(self, investimento_id):
        return self.session.query(Atualizacao).filter(Atualizacao.investimento_id == investimento_id).all()
    
    def buscar_por_id(self, id_atualizacao):
        return self.session.get(Atualizacao, id_atualizacao)

    def adicionar_Atualizacao(self, atualizacao):
        self.session.add(atualizacao)
        self.session.flush()
        return atualizacao
    
    def remover_Atualizacao(self, id_atualizacao):
        obj_Atualizacao = self.buscar_por_id(id_atualizacao)
        if obj_Atualizacao is None:
            return False
        self.session.delete(obj_Atualizacao)
        self.session.flush()