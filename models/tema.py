from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class Tema(Base):
    __tablename__ = 'tema'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    criado_em = Column(DateTime, default=current_time)

    def __repr__(self):
        return f"Tema(id={self.id}, nome='{self.nome}', criado_em={self.criado_em})"
