from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from globais import *
import utils.files_manager as fm
import logging

# Configuração do log para SQLAlchemy
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Caminho para o banco de dados SQLite
DATABASE_URL = f"sqlite:///{PASTA_BASE}{SQL_FILE}"

# Garantir que a pasta do banco de dados exista
fm.FileManager(PASTA_BASE).create_folder(PASTA_BASE)

# Configuração do SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

 
def get_db():
    """Função para obter a sessão do banco de dados """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
