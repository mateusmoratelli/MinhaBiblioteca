from sqlalchemy.orm import Session
from models.livros import Livros

# CRUD para Livros
def create_livro(db: Session, titulo: str, autor: str, editora: str, genero: str, isbn: str, paginas: int, ano_publicacao: int, capa: str, pdf: str, classficacao: int, sinopse: str):
   livro = Livros(
       titulo=titulo,
       autor=autor,
       editora=editora,
       genero=genero,
       isbn=isbn,
       paginas=paginas,
       ano_publicacao=ano_publicacao,
       capa=capa,
       pdf=pdf,
       classficacao=classficacao,
       sinopse=sinopse
   )
   db.add(livro)
   db.commit()
   db.refresh(livro)
   return livro

def get_livro_by_id(db: Session, livro_id: int):
   return db.query(Livros).filter(Livros.id == livro_id).first()


def get_livro_by_titulo(db: Session, titulo: str):
   return db.query(Livros).filter(Livros.titulo == titulo).first()



def get_all_livros(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Livros).order_by(Livros.titulo).offset(skip).limit(limit).all()



def update_livro(db: Session, livro_id: int, titulo: str = None, autor: str = None, editora: str = None, genero: str = None, isbn: str = None, paginas: int = None, ano_publicacao: int = None, capa: str = None, pdf: str = None, classficacao: int = None, sinopse: str = None):
   livro = db.query(Livros).filter(Livros.id == livro_id).first()
   if livro:
       if titulo:
           livro.titulo = titulo
       if autor:
           livro.autor = autor
       if editora:
           livro.editora = editora
       if genero:
           livro.genero = genero
       if isbn:
           livro.isbn = isbn
       if paginas:
           livro.paginas = paginas
       if ano_publicacao:
           livro.ano_publicacao = ano_publicacao
       if capa:
           livro.capa = capa
       if pdf:
           livro.pdf = pdf
       if classficacao:
           livro.classficacao = classficacao
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
