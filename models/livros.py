from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class Livros(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    autor = Column(String)
    editora = Column(String)
    tema = Column(String)
    isbn = Column(String)
    paginas = Column(String)
    ano_publicacao = Column(String)
    capa = Column(String)
    pdf = Column(String)
    classficacao = Column(String)
    sinopse = Column(String)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão


    def __repr__(self):
        return (f"Livros(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', "
                f"editora='{self.editora}', tema='{self.tema}', isbn='{self.isbn}', "
                f"paginas={self.paginas}, ano_publicacao={self.ano_publicacao}, capa='{self.capa}', "
                f"pdf='{self.pdf}', classficacao={self.classficacao}, sinopse='{self.sinopse}', "
                f"criado_em={self.criado_em})")