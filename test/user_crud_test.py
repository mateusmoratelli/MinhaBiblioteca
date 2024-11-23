from database import db_setup
from database.db_setup import SessionLocal
from crud.user import create_user, get_user, update_user, delete_user, get_users
from crud.livros_categorias import create_livros_categorias, get_livros_categorias, update_livros_categorias, delete_livros_categorias, get_all_livros_categorias
from crud.categorias import create_categoria, get_categoria, update_categoria, delete_categoria, get_all_categorias
from crud.livros import create_livro, get_livro, update_livro, delete_livro, get_all_livros
from datetime import datetime

def test_grava_usuario():
   db = SessionLocal()
   x = create_user(db, nome="John DoeC", email="ajoxhn.doe@example.scom", senha="spassword")
   print(f"xxxxxxxxxxxxxxxxxxxx {x}")
   assert x == x


def run_crud_operations():
   db = SessionLocal()
   try:
       # Operações CRUD para User
       user = create_user(db, nome="John DoeC", email="ajoxhn.doe@example.com", senha="spassword")
       print(f"Created User: {user}")

       user = get_user(db, user_id=user.id)
       print(f"Retrieved User: {user}")

       updated_user = update_user(db, user_id=user.id, nome="Johccnny Doe")
       print(f"Updated User: {updated_user}")

       all_users = get_users(db)
       print(f"All Users: {all_users}")

    #    delete_user(db, user_id=user.id)
       print(f"Deleted User: {user.id}")

       # Operações CRUD para LivrosCategorias
       livros_categorias = create_livros_categorias(db, livro_id=1, categoria_id=1)
       print(f"Created LivrosCategorias: {livros_categorias}")

       livros_categorias = get_livros_categorias(db, livros_categorias_id=livros_categorias.id)
       print(f"Retrieved LivrosCategorias: {livros_categorias}")

       updated_livros_categorias = update_livros_categorias(db, livros_categorias_id=livros_categorias.id, livro_id=2)
       print(f"Updated LivrosCategorias: {updated_livros_categorias}")

       all_livros_categorias = get_all_livros_categorias(db)
       print(f"All LivrosCategorias: {all_livros_categorias}")

    #    delete_livros_categorias(db, livros_categorias_id=livros_categorias.id)
       print(f"Deleted LivrosCategorias: {livros_categorias.id}")

       # Operações CRUD para Categorias
       categoria = create_categoria(db, categoria="Ficção")
       print(f"Created Categoria: {categoria}")

       categoria = get_categoria(db, categoria_id=categoria.id)
       print(f"Retrieved Categoria: {categoria}")

       updated_categoria = update_categoria(db, categoria_id=categoria.id, categoria="Fantasia")
       print(f"Updated Categoria: {updated_categoria}")

       all_categorias = get_all_categorias(db)
       print(f"All Categorias: {all_categorias}")

    #    delete_categoria(db, categoria_id=categoria.id)
       print(f"Deleted Categoria: {categoria.id}")

       # Operações CRUD para Livros
       livro = create_livro(
           db,
           titulo="O Senhor dos Anéis",
           autor="J.R.R. Tolkien",
           paginas=1216,
           ano_publicacao=1954,
           genero="Fantasia",
           capa="URL da capa",
           pdf="URL do PDF",
           classficacao=5,
           editora="Allen & Unwin",
           isbn="978-0544003415",
           sinopse="Uma saga épica..."
       )
       print(f"Created Livro: {livro}")

       livro = get_livro(db, livro_id=livro.id)
       print(f"Retrieved Livro: {livro}")

       updated_livro = update_livro(db, livro_id=livro.id, titulo="O Hobbit")
       print(f"Updated Livro: {updated_livro}")

       all_livros = get_all_livros(db)
       print(f"All Livros: {all_livros}")

    #    delete_livro(db, livro_id=livro.id)
       print(f"Deleted Livro: {livro.id}")

   finally:
       db.close()

if __name__ == "__main__":
   db_setup.init_db()  # Ensure the database is initialized
   run_crud_operations()  # Run CRUD operations
