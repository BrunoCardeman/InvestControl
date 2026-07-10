from app.database.connection import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Investimento(Base):

    __tablename__ = "investimentos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(80),nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"), nullable=False)
    valor_investimento: Mapped[float] = mapped_column()
    valor_atual: Mapped[float] = mapped_column()
    rentabilidade_Atual: Mapped[float] = mapped_column()
    data_Ultima_Atualizacao: Mapped[str] = mapped_column()
    dataCriacao: Mapped[str] = mapped_column()
    observacoes: Mapped[str] = mapped_column()
    ativo: Mapped[bool] = mapped_column()

    categoria: Mapped["Categoria"] = relationship(back_populates="investimentos")
    atualizacoes: Mapped[list["Atualizacao"]] = relationship(back_populates="investimentos")

