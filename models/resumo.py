"""
Arquivo: models/resumo.py
Descrição: Define a estrutura de dados para o modelo 'Resumo'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Representa resumos de livros no banco de dados.
    - Inclui informações como ID do usuário, ID do livro, conteúdo do resumo, e progresso de leitura.
"""


from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base, engine  # Importa o engine para criação das tabelas
from utils.time_utils import current_time

class Resumo(Base):
    __tablename__ = 'resumo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String)
    idlivro = Column(Integer)
    tituloResumo = Column(String)
    resumo = Column(String)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão
    

    # addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return (f"Resumo(id={self.id}, usuario={self.usuario}, idlivro={self.idlivro}, tituloResumo='{self.tituloResumo}', "
                f"resumo='{self.resumo}', criado_em={self.criado_em})")
    
# Inicializa a tabela no banco de dados ao importar o arquivo
Base.metadata.create_all(bind=engine)