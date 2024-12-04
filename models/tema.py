"""
Arquivo: models/tema.py
Descrição: Define a estrutura de dados para o modelo 'Tema'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Representa temas associados aos livros no banco de dados.
    - Inclui informações como nome do tema e data de criação.
"""


from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base, engine  # Importa o engine para criação das tabelas
from utils.time_utils import current_time

class Tema(Base):
    __tablename__ = 'tema'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tema = Column(String, nullable=False)
    criado_em = Column(DateTime, default=current_time)

    def __repr__(self):
        return f"Tema(id={self.id}, tema='{self.tema}', criado_em={self.criado_em})"


# Inicializa a tabela no banco de dados ao importar o arquivo
Base.metadata.create_all(bind=engine)