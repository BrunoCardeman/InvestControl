
from app.models.atualizacao import Atualizacao
from datetime import date

class InvestimentoService:
        
    def __init__(self, investimento_repo, atualizacao_repo):
        self.investimento_repo = investimento_repo
        self.atualizacao_repo = atualizacao_repo

    def calcular_rendimento(self,valor_atual, valor_anterior, aporte):
        if valor_anterior == 0: 
            return 0
        return valor_atual - valor_anterior - aporte
    
    def calcular_rendimento_percentual(self,valor_anterior,rendimento):
        if valor_anterior == 0:
            return 0
        return rendimento/valor_anterior
    
    def registrar_atualizacao_mensal(self, investimento_id, valor_atual, aporte):
        investimento = self.investimento_repo.buscar_por_id(investimento_id)

        rendimento = self.calcular_rendimento(valor_atual, investimento.valor_atual, aporte)


        novo_atualizacao = Atualizacao(
            investimento_id=investimento_id,
            valor_atual=valor_atual,
            aporte=aporte,
            rendimento=rendimento,
            data_Ultima_Atualizacao=date.today()
        )

        self.atualizacao_repo.adicionar(novo_atualizacao)
        
        investimento.valor_investimento = investimento.valor_investimento + aporte

        rendimento_total = self.calcular_rendimento(valor_atual, investimento.valor_investimento, 0)
        rentabilidade_total = self.calcular_rendimento_percentual(investimento.valor_investimento, rendimento_total)

        investimento.valor_atual = valor_atual
        investimento.rendimento_Atual = rendimento_total
        investimento.rentabilidade_Atual = rentabilidade_total
        investimento.data_Ultima_Atualizacao = date.today()

        self.investimento_repo.atualizar(investimento)