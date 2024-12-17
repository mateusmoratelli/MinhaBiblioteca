"""
Arquivo: crud/tema.py
Descrição: Contém funções de manipulação de dados (CRUD) para o modelo 'Tema'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Funções para criar, ler, atualizar e deletar temas de livros.
    - Inclui lógica para listar temas disponíveis.
"""
from sqlalchemy.orm import sessionmaker
from database.db_setup import engine
# from sqlalchemy.orm import Session
from models.tema import Tema

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()


# CRUD para tema
def create_tema(tema: str):
   tema = Tema(tema=tema)
   session.add(tema)
   session.commit()
   session.refresh(tema)
   return tema


def get_tema_by_id(tema_id: int):
   return session.query(Tema).filter(Tema.id == tema_id).first()


def get_tema_by_name(tema: str):
   return session.query(Tema).filter(Tema.tema == tema).all()


def search_tema_by_name(search_term: str):
    """
    Busca gêneros que contenham o termo de pesquisa (case insensitive).
    
    :param db: Sessão do banco de dados.
    :param search_term: Termo a ser pesquisado.
    :return: Lista de objetos `Tema` correspondentes. 
    """
    search_pattern = f"%{search_term}%"
    return session.query(Tema).filter(Tema.tema.ilike(search_pattern)).all()
    


def get_all_tema(skip: int = 0, limit: int = 999999):
   db_list = session.query(Tema).order_by(Tema.tema).offset(skip).limit(limit).all()
   return db_list


def update_tema(tema_id: int, tema: str = None):
   tema_obj = session.query(Tema).filter(Tema.id == tema_id).first()
   if tema_obj:
       if tema:
           tema_obj.tema = tema
       session.commit()
       session.refresh(tema_obj)
   return tema_obj


def delete_tema(tema_id: int):
   tema = session.query(Tema).filter(Tema.id == tema_id).first()
   if tema:
       session.delete(tema)
       session.commit()
   return tema