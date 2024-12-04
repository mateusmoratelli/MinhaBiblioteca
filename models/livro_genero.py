from sqlalchemy import Column, Integer, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class LivroGenero(Base):
    __tablename__ = 'livrogenero'

    id = Column(Integer, primary_key=True, autoincrement=True)
    livro_id = Column(Integer, nullable=False)
    genero_id = Column(Integer, nullable=False)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão


    def __repr__(self):
        return (f"LivroGenero(id={self.id}, livro_id={self.livro_id}, "
                f"genero_id={self.genero_id}, criado_em={self.criado_em})")