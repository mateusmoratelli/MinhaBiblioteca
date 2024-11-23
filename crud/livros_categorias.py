from sqlalchemy.orm import Session
from models.livros_categorias import LivrosCategorias

# CRUD para LivrosCategorias
def create_livros_categorias(db: Session, livro_id: int, categoria_id: int):
   livros_categorias = LivrosCategorias(livro_id=livro_id, categoria_id=categoria_id)
   db.add(livros_categorias)
   db.commit()
   db.refresh(livros_categorias)
   return livros_categorias

def get_livros_categorias(db: Session, livros_categorias_id: int):
   return db.query(LivrosCategorias).filter(LivrosCategorias.id == livros_categorias_id).first()

def get_all_livros_categorias(db: Session, skip: int = 0, limit: int = 10):
   return db.query(LivrosCategorias).offset(skip).limit(limit).all()

def update_livros_categorias(db: Session, livros_categorias_id: int, livro_id: int = None, categoria_id: int = None):
   livros_categorias = db.query(LivrosCategorias).filter(LivrosCategorias.id == livros_categorias_id).first()
   if livros_categorias:
       if livro_id:
           livros_categorias.livro_id = livro_id
       if categoria_id:
           livros_categorias.categoria_id = categoria_id
       db.commit()
       db.refresh(livros_categorias)
   return livros_categorias

def delete_livros_categorias(db: Session, livros_categorias_id: int):
   livros_categorias = db.query(LivrosCategorias).filter(LivrosCategorias.id == livros_categorias_id).first()
   if livros_categorias:
       db.delete(livros_categorias)
       db.commit()
   return livros_categorias
