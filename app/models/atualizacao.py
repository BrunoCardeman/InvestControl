from app.database.connection import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

class Atualizacao(Base):

    __tablename__ = "atualizacoes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    investimento_id: Mapped[int] = mapped_column(ForeignKey("investimentos.id"), nullable=False)
    valor_atual: Mapped[float] = mapped_column()
    aporte: Mapped[float] = mapped_column()
    rentabilidade: Mapped[float] = mapped_column()
    data_Ultima_Atualizacao: Mapped[str] = mapped_column()
    
    investimentos: Mapped["Investimento"] = relationship(back_populates="atualizacoes")
