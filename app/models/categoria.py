from app.database.connection import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Categoria(Base):

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(80),nullable=False)
    icone: Mapped[str|None] = mapped_column(String(50))
    cor: Mapped[str|None] = mapped_column(String(50))

    investimentos: Mapped[list["Investimento"]] = relationship(back_populates="categoria")
