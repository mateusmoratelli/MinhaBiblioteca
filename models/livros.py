from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class Livros(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    autor = Column(String)
    paginas = Column(Integer)
    ano_publicacao = Column(Integer)
    genero = Column(String)
    capa = Column(String)
    pdf = Column(String)
    classficacao = Column(Integer)
    editora = Column(String)
    isbn = Column(String)
    sinopse = Column(String)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão


    def __repr__(self):
        return f"<Livros(titulo='{self.titulo}', autor='{self.autor}', paginas='{self.paginas}', ano_publicacao='{self.ano_publicacao}' )>"