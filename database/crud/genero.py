from sqlalchemy.orm import Session
from models.genero import Genero

# CRUD para genero
def create_genero(db: Session, genero: str):
   genero = Genero(genero=genero)
   db.add(genero)
   db.commit()
   db.refresh(genero)
   return genero


def get_genero_by_id(db: Session, genero_id: int):
   return db.query(Genero).filter(Genero.id == genero_id).first()


def get_genero_by_name(db: Session, genero: str):
   return db.query(Genero).filter(Genero.genero == genero).all()


def search_genero_by_name(db: Session, search_term: str):
    """
    Busca gêneros que contenham o termo de pesquisa (case insensitive).
    
    :param db: Sessão do banco de dados.
    :param search_term: Termo a ser pesquisado.
    :return: Lista de objetos `Genero` correspondentes. 
    """
    search_pattern = f"%{search_term}%"
    return db.query(Genero).filter(Genero.genero.ilike(search_pattern)).all()
    


def get_all_genero(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Genero).order_by(Genero.genero).offset(skip).limit(limit).all()


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