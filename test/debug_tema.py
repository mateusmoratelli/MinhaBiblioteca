from database.db_setup import Base, engine
from models.tema import Tema

def inicio():
    print("Tabelas antes da criação:", Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    print("Tabelas depois da criação:", Base.metadata.tables.keys())
