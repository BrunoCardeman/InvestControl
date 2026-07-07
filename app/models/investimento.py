from app.database.connection import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.categoria import Categoria

class Investimento(Base):

    __tablename__ = "investimentos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(80),nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("Categorias.id"), nullable=False)
    valor_investimento: Mapped[int] = mapped_column()
    valor_atual: Mapped[int] = mapped_column()
    rentabilidade_Atual: Mapped[int] = mapped_column()
    aporte: Mapped[int] = mapped_column()
    data_Ultima_Atualização: Mapped[str] = mapped_column()
    dataCriacao: Mapped[str] = mapped_column()
    obsercacoes: Mapped[str] = mapped_column()
    ativo: Mapped[bool] = mapped_column()

