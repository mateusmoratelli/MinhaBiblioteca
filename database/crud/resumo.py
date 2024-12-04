"""
Arquivo: crud/resumo.py
Descrição: Contém funções de manipulação de dados (CRUD) para o modelo 'Resumo'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Funções para criar, ler, atualizar e deletar resumos de livros.
    - Inclui lógica para associar resumos a usuários e livros.
"""

from sqlalchemy.orm import Session
from models.resumo import Resumo

# CRUD para Resumo
def create_resumo(db: Session, idusuario: int, idlivro: int, resumo: str, paginasLidas: int):
   resumo_obj = Resumo(idusuario=idusuario, idlivro=idlivro, resumo=resumo, paginasLidas=paginasLidas)
   db.add(resumo_obj)
   db.commit()
   db.refresh(resumo_obj)
   return resumo_obj



def get_resumo(db: Session, resumo_id: int):
   return db.query(Resumo).filter(Resumo.id == resumo_id).first()



def get_all_resumos(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Resumo).offset(skip).limit(limit).all()



def update_resumo(db: Session, resumo_id: int, idusuario: int = None, idlivro: int = None, resumo: str = None, paginasLidas: int = None):
   resumo_obj = db.query(Resumo).filter(Resumo.id == resumo_id).first()
   if resumo_obj:
       if idusuario:
           resumo_obj.idusuario = idusuario
       if idlivro:
           resumo_obj.idlivro = idlivro
       if resumo:
           resumo_obj.resumo = resumo
       if paginasLidas is not None:
           resumo_obj.paginasLidas = paginasLidas
       db.commit()
       db.refresh(resumo_obj)
   return resumo_obj



def delete_resumo(db: Session, resumo_id: int):
   resumo_obj = db.query(Resumo).filter(Resumo.id == resumo_id).first()
   if resumo_obj:
       db.delete(resumo_obj)
       db.commit()
   return resumo_obj
