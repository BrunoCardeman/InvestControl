from app.database.connection import SessionLocal
from app.repositories.categoria_repository import CategoriaRepository
from app.repositories.investimento_repository import InvestimentoRepository
from app.repositories.atualizacao_repository import AtualizacaoRepository
from app.services.investimento_service import InvestimentoService
from app.models.categoria import Categoria
from app.models.investimento import Investimento
from datetime import date

from app.database.connection import init_db

init_db()

sessao = SessionLocal()

categoria_repo = CategoriaRepository(sessao)
investimento_repo = InvestimentoRepository(sessao)
atualizacao_repo = AtualizacaoRepository(sessao)

service = InvestimentoService(investimento_repo, atualizacao_repo)

# --- Preparacao: cria uma categoria e um investimento inicial de teste ---
categoria_teste = Categoria(nome="Tesouro Direto", icone="banco", cor="#4CAF50")
categoria_repo.adicionar(categoria_teste)

investimento_teste = Investimento(
    nome="Tesouro Selic 2029",
    categoria_id=categoria_teste.id,
    valor_investimento=1000.0,
    valor_atual=1000.0,
    rendimento_Atual=0.0,
    rentabilidade_Atual=0.0,
    data_Ultima_Atualizacao=str(date.today()),
    dataCriacao=str(date.today()),
    observacoes="Investimento de teste",
    ativo=True,
)
investimento_repo.adicionar(investimento_teste)

print("Investimento criado:")
print(f"  valor_investimento={investimento_teste.valor_investimento}")
print(f"  valor_atual={investimento_teste.valor_atual}")

# --- Teste: registra uma atualizacao mensal ---
# Simula: aportou mais R$200, e o valor foi para R$1300
service.registrar_atualizacao_mensal(
    investimento_id=investimento_teste.id,
    valor_atual=1300.0,
    aporte=200.0,
)

print("\nApos registrar atualizacao mensal:")
print(f"  valor_investimento={investimento_teste.valor_investimento}  (esperado: 1200.0)")
print(f"  valor_atual={investimento_teste.valor_atual}  (esperado: 1300.0)")
print(f"  rendimento_Atual={investimento_teste.rendimento_Atual}  (esperado: 100.0)")
print(f"  rentabilidade_Atual={investimento_teste.rentabilidade_Atual:.4f}  (esperado: ~0.0833)")

# Confere o historico criado na tabela Atualizacao
historico = atualizacao_repo.listar_por_investimento(investimento_teste.id)
print("\nHistorico de atualizacoes deste investimento:")
for a in historico:
    print(f"  - data={a.data_Ultima_Atualizacao}, valor_atual={a.valor_atual}, aporte={a.aporte}, rendimento={a.rendimento}")

# Desfaz tudo - nao salva nada permanentemente
sessao.rollback()
print("\nRollback feito - nada foi salvo permanentemente no banco.")

sessao.close()