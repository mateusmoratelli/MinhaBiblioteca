"""
Arquivo: crud/setup.py
Descrição: Contém funções de manipulação de dados (CRUD) para o modelo 'Setup'.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Funções para gerenciar configurações do sistema.
    - Utilizado para armazenar valores de configuração chave-valor no banco de dados.
"""
from sqlalchemy.orm import sessionmaker
from database.db_setup import engine
# from sqlalchemy.orm import Session
from models.setup import Setup

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()

# CRUD para Setup
def create_setup(configuracao: str, valor: str):
    """
    Cria um novo registro de Setup.

    :param configuracao: Nome da configuração.
    :param valor: Valor da configuração.
    :return: Objeto `Setup` criado.
    """
    setup = Setup(configuracao=configuracao, valor=valor)
    session.add(setup)
    session.commit()
    session.refresh(setup)
    return setup


def get_setup_by_id(setup_id: int):
    """
    Obtém um registro de Setup pelo ID.

    :param setup_id: ID do registro.
    :return: Objeto `Setup` correspondente ou None.
    """
    return session.query(Setup).filter(Setup.id == setup_id).first()


def get_setup_by_name(configuracao: str):
    """
    Obtém registros de Setup pelo nome da configuração.

    :param configuracao: Nome da configuração.
    :return: Lista de objetos `Setup` correspondentes.
    """
    return session.query(Setup).filter(Setup.configuracao == configuracao).all()


def search_setup_by_name(search_term: str):
    """
    Busca configurações que contenham o termo de pesquisa (case insensitive).

    :param db: Sessão do banco de dados.
    :param search_term: Termo a ser pesquisado.
    :return: Lista de objetos `Setup` correspondentes.
    """
    search_pattern = f"%{search_term}%"
    return session.query(Setup).filter(Setup.configuracao.ilike(search_pattern)).all()


def get_all_setup(skip: int = 0, limit: int = 10):
    """
    Obtém todos os registros de Setup com paginação.

    :param skip: Número de registros a pular.
    :param limit: Número máximo de registros a retornar.
    :return: Lista de objetos `Setup`.
    """
    return session.query(Setup).order_by(Setup.configuracao).offset(skip).limit(limit).all()


def update_setup(setup_id: int, configuracao: str = None, valor: str = None):
    """
    Atualiza um registro de Setup pelo ID.

    :param setup_id: ID do registro a ser atualizado.
    :param configuracao: Novo nome da configuração (opcional).
    :param valor: Novo valor da configuração (opcional).
    :return: Objeto `Setup` atualizado ou None.
    """
    setup_obj = session.query(Setup).filter(Setup.id == setup_id).first()
    if setup_obj:
        if configuracao:
            setup_obj.configuracao = configuracao
        if valor:
            setup_obj.valor = valor
        session.commit()
        session.refresh(setup_obj)
    return setup_obj


def delete_setup(setup_id: int):
    """
    Exclui um registro de Setup pelo ID.

    :param setup_id: ID do registro a ser excluído.
    :return: Objeto `Setup` excluído ou None.
    """
    setup = session.query(Setup).filter(Setup.id == setup_id).first()
    if setup:
        session.delete(setup)
        session.commit()
    return setup
