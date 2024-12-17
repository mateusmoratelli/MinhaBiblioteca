"""
Arquivo: crud/usuario.py
Descrição: Contém funções de manipulação de dados (CRUD) para o modelo 'Usuário'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Funções para criar, ler, atualizar e deletar usuários do sistema.
    - Pode incluir funcionalidades adicionais, como autenticação e associações.
"""

from sqlalchemy.orm import sessionmaker
from database.db_setup import engine
# from sqlalchemy.orm import Session
from models.usuario import Usuario

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()

# CRUD para Usuario
def create_user(nome):
   user = Usuario(nome=nome)
   session.add(user)
   session.commit()
   session.refresh(user)
   return user



def get_user_by_id(user_id: int):
   return session.query(Usuario).filter(Usuario.id == user_id).first()



def get_user_by_name(nome: str):
   listaDB = session.query(Usuario).filter(Usuario.nome == nome).first()
   return listaDB



def get_users(skip: int = 0, limit: int = 10):
   return session.query(Usuario).order_by(Usuario.nome).offset(skip).limit(limit).all()



def update_user(user_id: int, nome: str = None):
   user = session.query(Usuario).filter(Usuario.id == user_id).first()
   if user:
       if nome:
           user.nome = nome
       session.commit()
       session.refresh(user)
   return user



def delete_user(user_id: int):
   user = session.query(Usuario).filter(Usuario.id == user_id).first()
   if user:
       session.delete(user)
       session.commit()
   return user
