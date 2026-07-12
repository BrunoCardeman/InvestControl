from app.database.connection import SessionLocal
from app.repositories.categoria_repository import CategoriaRepository
from app.repositories.investimento_repository import InvestimentoRepository
from app.models.categoria import Categoria
from app.models.investimento import Investimento
from app.models.atualizacao import Atualizacao
sessao = SessionLocal()

categoria_repo = CategoriaRepository(sessao)
investimento_repo = InvestimentoRepository(sessao)

# Cria uma categoria de teste
nova_categoria = Categoria(nome="CDB", icone="banco", cor="#4CAF50")
categoria_repo.adicionar_Categoria(nova_categoria)

print("Categoria criada com id:", nova_categoria.id)

# Lista todas as categorias (ainda dentro da mesma sessao, sem commit)
todas_categorias = categoria_repo.listar_todos()
print("Categorias visiveis nesta sessao (ainda nao commitadas):")
for c in todas_categorias:
    print(f"  - id={c.id}, nome={c.nome}, icone={c.icone}, cor={c.cor}")

# Cria um investimento vinculado a essa categoria
novo_investimento = Investimento(
    nome="Tesouro Selic 2029",
    categoria_id=nova_categoria.id,
    valor_investimento=15000.0,
    valor_atual=15000.0,
    rentabilidade_Atual=0.0,
    data_Ultima_Atualizacao="2026-07-01",
    dataCriacao="2026-07-01",
    observacoes="Teste inicial",
    ativo=True,
)
investimento_repo.adicionar_Investimento(novo_investimento)

print("\nInvestimento criado com id:", novo_investimento.id)

todos_investimentos = investimento_repo.listar_todos()
print("Investimentos visiveis nesta sessao (ainda nao commitados):")
for i in todos_investimentos:
    print(f"  - id={i.id}, nome={i.nome}, categoria_id={i.categoria_id}, valor_atual={i.valor_atual}")

# Desfaz tudo -> nada disso fica salvo de verdade no banco
sessao.rollback()
print("\nRollback feito - nada foi salvo permanentemente no banco.")

sessao.close()