"""
Arquivo: database_creator.py
Descrição: Classe para criação e configuração da base de dados SQLite sem o uso de bibliotecas ORM.
Autor: Mateus Moratelli
Data de Criação: 2024-12-04
Última Modificação: 2024-12-04
Detalhes:
    - Criação das tabelas para armazenar dados relacionados ao sistema de livros.
"""

import sqlite3

class DatabaseCreator:
    def __init__(self, db_path: str):
        """
        Inicializa o criador de banco de dados.

        :param db_path: Caminho para o arquivo do banco de dados.
        """
        self.db_path = db_path

    def create_tables(self):
        """
        Cria todas as tabelas necessárias no banco de dados.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Criação da tabela `tema`
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tema (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Criação da tabela `livros`
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT,
                    editora TEXT,
                    tema TEXT,
                    isbn TEXT,
                    paginas INTEGER,
                    ano_publicacao INTEGER,
                    capa TEXT,
                    pdf TEXT,
                    classficacao INTEGER,
                    sinopse TEXT,
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Criação da tabela `genero`
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS genero (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Criação da tabela `resumo`
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS resumo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    idusuario INTEGER NOT NULL,
                    idlivro INTEGER NOT NULL,
                    resumo TEXT,
                    paginas_lidas INTEGER,
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Criação da tabela `setup`
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS setup (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    configuracao TEXT NOT NULL,
                    valor TEXT NOT NULL,
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Criação da tabela `usuario`
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conn.commit()

if __name__ == "__main__":
    # Caminho para o banco de dados
    DATABASE_PATH = "database.db"

    # Inicializa o criador e cria as tabelas
    db_creator = DatabaseCreator(DATABASE_PATH)
    db_creator.create_tables()
    print(f"Tabelas criadas no banco de dados '{DATABASE_PATH}'.")
