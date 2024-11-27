from sqlalchemy.orm import Session
from models.genero import Genero

# CRUD para genero
def create_genero(db: Session, genero: str):
   genero = Genero(genero=genero)
   db.add(genero)
   db.commit()
   db.refresh(genero)
   return genero

def get_genero(db: Session, genero_id: int):
   return db.query(Genero).filter(Genero.id == genero_id).first()

def get_all_genero(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Genero).offset(skip).limit(limit).all()

def update_genero(db: Session, genero_id: int, genero: str = None):
   genero_obj = db.query(Genero).filter(Genero.id == genero_id).first()
   if genero_obj:
       if genero:
           genero_obj.genero = genero
       db.commit()
       db.refresh(genero_obj)
   return genero_obj

def delete_genero(db: Session, genero_id: int):
   genero = db.query(Genero).filter(Genero.id == genero_id).first()
   if genero:
       db.delete(genero)
       db.commit()
   return genero
