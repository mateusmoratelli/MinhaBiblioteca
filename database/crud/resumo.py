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

from sqlalchemy import and_
from sqlalchemy.orm import Session
from models.resumo import Resumo

# CRUD para Resumo
def create_resumo(db: Session, usuario: str, idlivro: int, tituloResumo: str, resumo: str):
   resumo_obj = Resumo(usuario=usuario, idlivro=idlivro, tituloResumo=tituloResumo, resumo=resumo)
   db.add(resumo_obj)
   db.commit()
   db.refresh(resumo_obj)
   return resumo_obj



def get_resumo_livro(db: Session, idlivro: int, usuario: str):
    lstResumo =  db.query(Resumo).filter(
        and_(
            Resumo.idlivro == idlivro,
            Resumo.usuario == usuario
        )
    ).all()
    return lstResumo



def get_all_resumos(db: Session, skip: int = 0, limit: int = 10):
   return db.query(Resumo).offset(skip).limit(limit).all()




def update_resumo(db: Session, resumo_id: int, usuario: str = None, idlivro: int = None, tituloResumo: str = None, resumo: str = None):
    resumo_obj = db.query(Resumo).filter(Resumo.id == resumo_id).first()
    if resumo_obj:
        if usuario:
            resumo_obj.usuario = usuario
        if idlivro:
            resumo_obj.idlivro = idlivro
        if tituloResumo:
            resumo_obj.tituloResumo = tituloResumo
        if resumo:
            resumo_obj.resumo = resumo
        db.commit()
        db.refresh(resumo_obj)
    return resumo_obj



def delete_resumo(db: Session, resumo_id: int):
   resumo_obj = db.query(Resumo).filter(Resumo.id == resumo_id).first()
   if resumo_obj:
       db.delete(resumo_obj)
       db.commit()
   return resumo_obj
