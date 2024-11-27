from sqlalchemy.orm import Session
from models.livro_genero import LivroGenero

# CRUD para LivroGenero
def create_livro_genero(db: Session, livro_id: int, genero_id: int):
   livro_genero = LivroGenero(livro_id=livro_id, genero_id=genero_id)
   db.add(livro_genero)
   db.commit()
   db.refresh(livro_genero)
   return livro_genero

def get_livro_genero(db: Session, livro_genero_id: int):
   return db.query(LivroGenero).filter(LivroGenero.id == livro_genero_id).first()

def get_all_livro_genero(db: Session, skip: int = 0, limit: int = 10):
   return db.query(LivroGenero).offset(skip).limit(limit).all()

def update_livro_genero(db: Session, livro_genero_id: int, livro_id: int = None, genero_id: int = None):
   livro_genero = db.query(LivroGenero).filter(LivroGenero.id == livro_genero_id).first()
   if livro_genero:
       if livro_id:
           livro_genero.livro_id = livro_id
       if genero_id:
           livro_genero.genero_id = genero_id
       db.commit()
       db.refresh(livro_genero)
   return livro_genero

def delete_livro_genero(db: Session, livro_genero_id: int):
   livro_genero = db.query(LivroGenero).filter(LivroGenero.id == livro_genero_id).first()
   if livro_genero:
       db.delete(livro_genero)
       db.commit()
   return livro_genero
