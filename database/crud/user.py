from sqlalchemy.orm import Session
from models.user import User

# CRUD para User
def create_user(db: Session, nome):
   user = User(nome=nome)
   db.add(user)
   db.commit()
   db.refresh(user)
   return user

def get_user_by_id(db: Session, user_id: int):
   return db.query(User).filter(User.id == user_id).first()

def get_user_by_name(db: Session, nome: str):
   listaDB = db.query(User).filter(User.nome == nome).first()
   return listaDB

def get_users(db: Session, skip: int = 0, limit: int = 10):
   return db.query(User).order_by(User.nome).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, nome: str = None):
   user = db.query(User).filter(User.id == user_id).first()
   if user:
       if nome:
           user.nome = nome
       db.commit()
       db.refresh(user)
   return user

def delete_user(db: Session, user_id: int):
   user = db.query(User).filter(User.id == user_id).first()
   if user:
       db.delete(user)
       db.commit()
   return user
