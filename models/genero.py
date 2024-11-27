from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class Genero(Base):
    __tablename__ = 'genero'

    id = Column(Integer, primary_key=True, autoincrement=True)
    genero = Column(String, nullable=False)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão


    def __repr__(self):
        return (f"Genero(id={self.id}, genero='{self.genero}', "
                f"criado_em={self.criado_em})")