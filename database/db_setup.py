import os
import pkgutil
import importlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from globais import *
import utils.files_manager as _fm
import logging  # Adicione aqui

# Configuração do log para SQLAlchemy
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

DATABASE_URL = f"sqlite:///{PASTA_BASE}{SQL_FILE}"

_fm.FileManager(PASTA_BASE).create_folder(PASTA_BASE)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # Importa todos os módulos no diretório `models`
    package_dir = os.path.join(os.path.dirname(__file__), '../models')
    for (module_loader, name, ispkg) in pkgutil.iter_modules([package_dir]):
        importlib.import_module(f"models.{name}")
        print(f"models.{name}")
    print("Tabelas registradas no metadata:", Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

# Inicialize o banco de dados ao importar este módulo
init_db()
