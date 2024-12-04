"""
Arquivo: models/usuario.py
Descrição: Define a estrutura de dados para o modelo 'Usuário'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Representa os usuários do sistema no banco de dados.
    - Inclui informações como nome do usuário e data de criação.
"""


from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base, engine  # Importa o engine para criação das tabelas
from utils.time_utils import current_time

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão
    

    # addresses = relationship("Address", back_populates="user")
    
    def __repr__(self):
        return (f"User(id={self.id}, nome='{self.nome}', "
                f"criado_em={self.criado_em})")

# Inicializa a tabela no banco de dados ao importar o arquivo
Base.metadata.create_all(bind=engine)