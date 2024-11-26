from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class Resumo(Base):
    __tablename__ = 'resumo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idusuario = Column(Integer, nullable=False)
    idlivro = Column(Integer, nullable=False)
    resumo = Column(String)
    paginasLidas = Column(Integer, default=0)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão
    

    # addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return (f"Resumo(id={self.id}, idusuario={self.idusuario}, idlivro={self.idlivro}, "
                f"resumo='{self.resumo}', paginasLidas={self.paginasLidas}, criado_em={self.criado_em})")