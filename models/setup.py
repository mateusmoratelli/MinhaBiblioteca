"""
Arquivo: models/setup.py
Descrição: Define a estrutura de dados para o modelo 'Setup'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Representa configurações chave-valor do sistema.
    - Utilizado para armazenar parâmetros personalizáveis.
"""



from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base, engine  # Importa o engine para criação das tabelas
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

# Inicializa a tabela no banco de dados ao importar o arquivo
Base.metadata.create_all(bind=engine)