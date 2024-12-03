from sqlalchemy.orm import Session
from models.categorias import Categoria

# CRUD para categoria
def create_categoria(db: Session, categoria: str):
   categoria = Categoria(categoria=categoria)
   db.add(categoria)
   db.commit()
   db.refresh(categoria)
   return categoria


def get_categoria_by_id(db: Session, categoria_id: int):
   return db.query(Categoria).filter(Categoria.id == categoria_id).first()


def get_categoria_by_name(db: Session, categoria: str):
   return db.query(Categoria).filter(Categoria.categoria == categoria).all()


def search_categoria_by_name(db: Session, search_term: str):
    """
    Busca gêneros que contenham o termo de pesquisa (case insensitive).
    
    :param db: Sessão do banco de dados.
    :param search_term: Termo a ser pesquisado.
    :return: Lista de objetos `Categoria` correspondentes. 
    """
    search_pattern = f"%{search_term}%"
    return db.query(Categoria).filter(Categoria.categoria.ilike(search_pattern)).all()
    


def get_all_categoria(db: Session, skip: int = 0, limit: int = 10):
   dbList = db.query(Categoria).order_by(Categoria.categoria).offset(skip).limit(limit).all()
   return dbList


def update_categoria(db: Session, categoria_id: int, categoria: str = None):
   categoria_obj = db.query(Categoria).filter(Categoria.id == categoria_id).first()
   if categoria_obj:
       if categoria:
           categoria_obj.categoria = categoria
       db.commit()
       db.refresh(categoria_obj)
   return categoria_obj


def delete_categoria(db: Session, categoria_id: int):
   categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
   if categoria:
       db.delete(categoria)
       db.commit()
   return categoria