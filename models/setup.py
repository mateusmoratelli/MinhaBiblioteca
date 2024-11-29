from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class Setup(Base):
    __tablename__ = 'setup'

    id = Column(Integer, primary_key=True, autoincrement=True)
    configuracao = Column(String, nullable=False)
    valor = Column(String, nullable=False)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão


    def __repr__(self):
        return (f"Setup(id={self.id}, configuracao='{self.configuracao}', valor='{self.valor}',"
                f"criado_em={self.criado_em})")