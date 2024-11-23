from sqlalchemy.orm import Session
from models.livros import Livros

# CRUD para Livros
def create_livro(db: Session, titulo: str, autor: str, paginas: int, ano_publicacao: int, genero: str, capa: str, pdf: str, classficacao: int, editora: str, isbn: str, sinopse: str):
   livro = Livros(
       titulo=titulo,
       autor=autor,
       paginas=paginas,
       ano_publicacao=ano_publicacao,
       genero=genero,
       capa=capa,
       pdf=pdf,
       classficacao=classficacao,
       editora=editora,
       isbn=isbn,
       sinopse=sinopse
   )
   db.add(livro)
   db.commit()
   db.refresh(livro)
   return livro

def get_livro(db: Session, livro_id: int):
   return db.query(Livros).filter(Livros.id == livro_id).first()

def get_all_livros(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Livros).offset(skip).limit(limit).all()

def update_livro(db: Session, livro_id: int, titulo: str = None, autor: str = None, paginas: int = None, ano_publicacao: int = None, genero: str = None, capa: str = None, pdf: str = None, classficacao: int = None, editora: str = None, isbn: str = None, sinopse: str = None):
   livro = db.query(Livros).filter(Livros.id == livro_id).first()
   if livro:
       if titulo:
           livro.titulo = titulo
       if autor:
           livro.autor = autor
       if paginas:
           livro.paginas = paginas
       if ano_publicacao:
           livro.ano_publicacao = ano_publicacao
       if genero:
           livro.genero = genero
       if capa:
           livro.capa = capa
       if pdf:
           livro.pdf = pdf
       if classficacao:
           livro.classficacao = classficacao
       if editora:
           livro.editora = editora
       if isbn:
           livro.isbn = isbn
       if sinopse:
           livro.sinopse = sinopse
       db.commit()
       db.refresh(livro)
   return livro

def delete_livro(db: Session, livro_id: int):
   livro = db.query(Livros).filter(Livros.id == livro_id).first()
   if livro:
       db.delete(livro)
       db.commit()
   return livro
