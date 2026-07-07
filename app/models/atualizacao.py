from app.database.connection import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.investimento import Investimento

class Atualizacao(Base):

    __tablename__ = "Atualizacao"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    investimento_id: Mapped[int] = mapped_column(ForeignKey("Investimento.id"), nullable=False)
    valor_atual: Mapped[int] = mapped_column()
    aporte: Mapped[int] = mapped_column()
    rentabilidade: Mapped[int] = mapped_column()
    data_Ultima_Atualização: Mapped[str] = mapped_column()
    

