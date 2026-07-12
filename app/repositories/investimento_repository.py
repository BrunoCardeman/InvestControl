from app.models.investimento import Investimento

class InvestimentoRepository:
    def __init__(self, session):
        self.session = session

    def listar_todos(self):
        return self.session.query(Investimento).all()

    def buscar_por_id(self, id_investimento):
        return self.session.get(Investimento, id_investimento)
    
    def atualizar(self, investimento):
        self.session.flush()

    def adicionar_Investimento(self, investimento):
        self.session.add(investimento)
        self.session.flush()
        return investimento

    def remover_Investimento(self, id_investimento):
        obj_Investimento = self.buscar_por_id(id_investimento)
        if obj_Investimento is None:
            return False
        self.session.delete(obj_Investimento)
        self.session.flush()

