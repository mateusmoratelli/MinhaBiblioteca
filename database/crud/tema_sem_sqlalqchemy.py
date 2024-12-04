"""
Arquivo: crud/tema.py
Descrição: Contém funções de manipulação de dados (CRUD) para o modelo 'Tema' sem o uso de SQLAlchemy.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Funções para criar, ler, atualizar e deletar temas de livros.
    - Inclui lógica para listar temas disponíveis.
"""

import sqlite3

# Configuração do banco de dados
DATABASE_PATH = "seu_caminho_para_o_arquivo_db/database.db"


def create_tema(tema: str):
    """
    Cria um novo tema.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tema (nome, criado_em) VALUES (?, datetime('now'))",
            (tema,),
        )
        conn.commit()
        return cursor.lastrowid


def get_tema_by_id(tema_id: int):
    """
    Obtém um tema pelo ID.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tema WHERE id = ?", (tema_id,))
        return cursor.fetchone()


def get_tema_by_name(tema: str):
    """
    Obtém temas pelo nome exato.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tema WHERE nome = ?", (tema,))
        return cursor.fetchall()


def search_tema_by_name(search_term: str):
    """
    Busca temas que contenham o termo de pesquisa (case insensitive).
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM tema WHERE nome LIKE ?", (f"%{search_term}%",)
        )
        return cursor.fetchall()


def get_all_tema(skip: int = 0, limit: int = 10):
    """
    Obtém todos os temas com paginação.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM tema ORDER BY nome LIMIT ? OFFSET ?", (limit, skip)
        )
        return cursor.fetchall()


def update_tema(tema_id: int, tema: str = None):
    """
    Atualiza o nome de um tema.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tema SET nome = ? WHERE id = ?", (tema, tema_id)
        )
        conn.commit()
        return cursor.rowcount > 0  # Retorna True se algo foi atualizado


def delete_tema(tema_id: int):
    """
    Deleta um tema pelo ID.
    """
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tema WHERE id = ?", (tema_id,))
        conn.commit()
        return cursor.rowcount > 0  # Retorna True se algo foi deletado
