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
from sqlalchemy.orm import sessionmaker
from database.db_setup import engine
from sqlalchemy import and_
# from sqlalchemy.orm import Session
from models.resumo import Resumo

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()

# CRUD para Resumo
def create_resumo(usuario: str, idlivro: int, tituloResumo: str, resumo: str):
   resumo_obj = Resumo(usuario=usuario, idlivro=idlivro, tituloResumo=tituloResumo, resumo=resumo)
   session.add(resumo_obj)
   session.commit()
   session.refresh(resumo_obj)
   return resumo_obj



def get_resumo_livro(idlivro: int, usuario: str):
    lstResumo =  session.query(Resumo).filter(
        and_(
            Resumo.idlivro == idlivro,
            Resumo.usuario == usuario
        )
    ).all()
    return lstResumo



def get_resumo_livro_by_id(id : int):
    lstResumo =  session.query(Resumo).filter(Resumo.id == id).all()
    return lstResumo



def get_all_resumos(skip: int = 0, limit: int = 10):
   return session.query(Resumo).offset(skip).limit(limit).all()



def update_resumo(resumo_id: int, usuario: str = None, idlivro: int = None, tituloResumo: str = None, resumo: str = None):
    resumo_obj = session.query(Resumo).filter(Resumo.id == resumo_id).first()
    if resumo_obj:
        if usuario:
            resumo_obj.usuario = usuario
        if idlivro:
            resumo_obj.idlivro = idlivro
        if tituloResumo:
            resumo_obj.tituloResumo = tituloResumo
        if resumo:
            resumo_obj.resumo = resumo
        session.commit()
        session.refresh(resumo_obj)
    return resumo_obj



def delete_resumo(resumo_id: int):
   resumo_obj = session.query(Resumo).filter(Resumo.id == resumo_id).first()
   if resumo_obj:
       session.delete(resumo_obj)
       session.commit()
   return resumo_obj
