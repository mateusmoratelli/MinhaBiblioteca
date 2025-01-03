"""
Arquivo: crud/livros.py
Descrição: Contém funções de manipulação de dados (CRUD) para o modelo 'Livros'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Funções para criar, ler, atualizar e deletar informações relacionadas a livros.
    - Implementação baseada no SQLAlchemy.
"""
from sqlalchemy.orm import sessionmaker
from database.db_setup import engine
# from sqlalchemy.orm import Session
from models.livros import Livros

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()

def create_livro(titulo: str, autor: str, editora: str, tema: str, isbn: str, paginas: int, ano_publicacao: int, capa: str, pdf: str, classficacao: int, sinopse: str):
   livro = Livros(
       titulo=titulo,
       autor=autor,
       editora=editora,
       tema=tema,
       isbn=isbn,
       paginas=paginas,
       ano_publicacao=ano_publicacao,
       capa=capa,
       pdf=pdf,
       classficacao=classficacao,
       sinopse=sinopse
   )
   session.add(livro)
   session.commit()
   session.refresh(livro)
   return livro



def get_livro_by_id(livro_id: int):
   return session.query(Livros).filter(Livros.id == livro_id).first()


def get_livro_by_titulo(titulo: str):
   return session.query(Livros).filter(Livros.titulo == titulo).first()


def get_livros_by_partial_titulo(partial_titulo: str, skip: int = 0, limit: int = 10):
    """
    Pesquisa livros cujo título contém o trecho fornecido (case insensitive).

    :param partial_titulo: Trecho do título para busca.
    :param skip: Número de registros para pular.
    :param limit: Número máximo de registros a retornar.
    :return: Lista de livros que contêm o trecho no título.
    """
    return (
        session.query(Livros)
        .filter(Livros.titulo.ilike(f"%{partial_titulo}%"))
        .order_by(Livros.titulo)
        .offset(skip)
        .limit(limit)
        .all()
    )



def get_all_livros(skip: int = 0, limit: int = 10):
   return session.query(Livros).order_by(Livros.titulo).offset(skip).limit(limit).all()



def update_livro(livro_id: int, titulo: str = None, autor: str = None, editora: str = None, tema: str = None, isbn: str = None, paginas: int = None, ano_publicacao: int = None, capa: str = None, pdf: str = None, classficacao: int = None, sinopse: str = None):
   livro = session.query(Livros).filter(Livros.id == livro_id).first()
   if livro:
       if titulo:
           livro.titulo = titulo
       if autor:
           livro.autor = autor
       if editora:
           livro.editora = editora
       if tema:
           livro.tema = tema
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
       if classficacao != None:
           livro.classficacao = classficacao
       if sinopse:
           livro.sinopse = sinopse
       session.commit()
       session.refresh(livro)
   return livro



def delete_livro(livro_id: int):
   livro = session.query(Livros).filter(Livros.id == livro_id).first()
   if livro:
       session.delete(livro)
       session.commit()
   return livro
