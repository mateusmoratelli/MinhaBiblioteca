from sqlalchemy.orm import Session
from models.tema import Tema

# CRUD para tema
def create_tema(db: Session, tema: str):
   tema = Tema(tema=tema)
   db.add(tema)
   db.commit()
   db.refresh(tema)
   return tema


def get_tema_by_id(db: Session, tema_id: int):
   return db.query(Tema).filter(Tema.id == tema_id).first()


def get_tema_by_name(db: Session, tema: str):
   return db.query(Tema).filter(Tema.tema == tema).all()


def search_tema_by_name(db: Session, search_term: str):
    """
    Busca gêneros que contenham o termo de pesquisa (case insensitive).
    
    :param db: Sessão do banco de dados.
    :param search_term: Termo a ser pesquisado.
    :return: Lista de objetos `Tema` correspondentes. 
    """
    search_pattern = f"%{search_term}%"
    return db.query(Tema).filter(Tema.tema.ilike(search_pattern)).all()
    


def get_all_tema(db: Session, skip: int = 0, limit: int = 10):
   dbList = db.query(Tema).order_by(Tema.tema).offset(skip).limit(limit).all()
   return dbList


def update_tema(db: Session, tema_id: int, tema: str = None):
   tema_obj = db.query(Tema).filter(Tema.id == tema_id).first()
   if tema_obj:
       if tema:
           tema_obj.tema = tema
       db.commit()
       db.refresh(tema_obj)
   return tema_obj


def delete_tema(db: Session, tema_id: int):
   tema = db.query(Tema).filter(Tema.id == tema_id).first()
   if tema:
       db.delete(tema)
       db.commit()
   return tema