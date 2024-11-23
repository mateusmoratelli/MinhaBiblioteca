from sqlalchemy.orm import Session
from models.categorias import Categorias

# CRUD para Categorias
def create_categoria(db: Session, categoria: str):
   categoria = Categorias(categoria=categoria)
   db.add(categoria)
   db.commit()
   db.refresh(categoria)
   return categoria

def get_categoria(db: Session, categoria_id: int):
   return db.query(Categorias).filter(Categorias.id == categoria_id).first()

def get_all_categorias(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Categorias).offset(skip).limit(limit).all()

def update_categoria(db: Session, categoria_id: int, categoria: str = None):
   categoria_obj = db.query(Categorias).filter(Categorias.id == categoria_id).first()
   if categoria_obj:
       if categoria:
           categoria_obj.categoria = categoria
       db.commit()
       db.refresh(categoria_obj)
   return categoria_obj

def delete_categoria(db: Session, categoria_id: int):
   categoria = db.query(Categorias).filter(Categorias.id == categoria_id).first()
   if categoria:
       db.delete(categoria)
       db.commit()
   return categoria
