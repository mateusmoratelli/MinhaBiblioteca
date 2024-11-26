from sqlalchemy import Column, Integer, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class LivrosCategorias(Base):
    __tablename__ = 'livro_categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    livro_id = Column(Integer, nullable=False)
    categoria_id = Column(Integer, nullable=False)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão


    def __repr__(self):
        return (f"LivrosCategorias(id={self.id}, livro_id={self.livro_id}, "
                f"categoria_id={self.categoria_id}, criado_em={self.criado_em})")