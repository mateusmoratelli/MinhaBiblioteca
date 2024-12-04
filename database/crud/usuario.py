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


from sqlalchemy.orm import Session
from models.usuario import Usuario

# CRUD para Usuario
def create_user(db: Session, nome):
   user = Usuario(nome=nome)
   db.add(user)
   db.commit()
   db.refresh(user)
   return user



def get_user_by_id(db: Session, user_id: int):
   return db.query(Usuario).filter(Usuario.id == user_id).first()



def get_user_by_name(db: Session, nome: str):
   listaDB = db.query(Usuario).filter(Usuario.nome == nome).first()
   return listaDB



def get_users(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Usuario).order_by(Usuario.nome).offset(skip).limit(limit).all()



def update_user(db: Session, user_id: int, nome: str = None):
   user = db.query(Usuario).filter(Usuario.id == user_id).first()
   if user:
       if nome:
           user.nome = nome
       db.commit()
       db.refresh(user)
   return user



def delete_user(db: Session, user_id: int):
   user = db.query(Usuario).filter(Usuario.id == user_id).first()
   if user:
       db.delete(user)
       db.commit()
   return user
