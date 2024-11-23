from sqlalchemy.orm import Session
from models.user import User

# CRUD para User
def create_user(db: Session, nome: str, email: str, senha: str):
   user = User(nome=nome, email=email, senha=senha)
   db.add(user)
   db.commit()
   db.refresh(user)
   return user

def get_user(db: Session, user_id: int):
   return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
   return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, nome: str = None, email: str = None, senha: str = None):
   user = db.query(User).filter(User.id == user_id).first()
   if user:
       if nome:
           user.nome = nome
       if email:
           user.email = email
       if senha:
           user.senha = senha
       db.commit()
       db.refresh(user)
   return user

def delete_user(db: Session, user_id: int):
   user = db.query(User).filter(User.id == user_id).first()
   if user:
       db.delete(user)
       db.commit()
   return user
