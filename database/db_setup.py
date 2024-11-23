import os
import pkgutil
import importlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./resumao_livros.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
   # Importa todos os módulos no diretório `models`
   package_dir = os.path.join(os.path.dirname(__file__), '../models')
   for (module_loader, name, ispkg) in pkgutil.iter_modules([package_dir]):
       importlib.import_module(f"models.{name}")
   Base.metadata.create_all(bind=engine)

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

# Inicialize o banco de dados ao importar este módulo
init_db()
