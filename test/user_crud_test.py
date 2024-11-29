from database.db_setup import SessionLocal
from database.crud.user import *
from database.crud.livro_genero import *
# from database.crud.genero import *
from database.crud.livros import *
from database.crud.resumo import *


def run_crud_operations():
   db = SessionLocal()
   try:
       # Operações CRUD para User
       user = create_user(db, nome="John Doe")
       print(f"Created User: {user}")

       user = get_user_by_id(db, user_id=user.id)
       print(f"Retrieved User: {user}")

       updated_user = update_user(db, user_id=user.id, nome="Johnny Doe")
       print(f"Updated User: {updated_user}")

       all_users = get_users(db)
       print(f"All Users: {all_users}")

       delete_user(db, user_id=user.id)
       print(f"Deleted User: {user.id}")

       # Operações CRUD para Livrosgenero
       livro_genero = create_livro_genero(db, livro_id=1, genero_id=1)
       print(f"Created Livrosgenero: {livro_genero}")

       livros_genero = get_livro_genero(db, livro_genero_id=livro_genero.id)
       print(f"Retrieved Livrosgenero: {livros_genero}")

       updated_livros_genero = update_livro_genero(db, livro_genero_id=livro_genero.id, livro_id=2)
       print(f"Updated Livrosgenero: {updated_livros_genero}")

       all_livros_genero = get_all_livro_genero(db)
       print(f"All Livrosgenero: {all_livros_genero}")

       delete_livro_genero(db, livro_genero_id=livro_genero.id)
       print(f"Deleted Livrosgenero: {livros_genero.id}")

    #    # Operações CRUD para genero
    #    genero = create_genero(db, genero="Ficção")
    #    print(f"Created Categoria: {genero}")

    #    genero = get_genero_by_id(db, genero_id=genero.id)
    #    print(f"Retrieved Categoria: {genero}")

    #    genex =  get_genero_by_name(db, genero="xxxx")
    #    print(genex)

    #    pedaco = search_genero_by_name(db, "Fic")
    #    print(f"Pedaço: {pedaco}")

    #    updated_genero = update_genero(db, genero_id=genero.id, genero="Fantasia")
    #    print(f"Updated Categoria: {updated_genero}")

    #    all_genero = get_all_genero(db)
    #    print(f"All genero: {all_genero}")


    #    delete_genero(db, genero_id=genero.id)
    #    print(f"Deleted Categoria: {genero.id}")

       # Operações CRUD para Livros
       livro = create_livro(
           db,
           titulo="O Senhor dos Anéis",
           autor="J.R.R. Tolkien",
           editora="Allen & Unwin",
           genero="Fantasia",
           isbn="978-0544003415",
           paginas=1216,
           ano_publicacao=1954,
           capa="URL da capa",
           pdf="URL do PDF",
           classficacao=5,
           sinopse="Uma saga épica..."
       )
       print(f"Created Livro: {livro}")

       livro = get_livro(db, livro_id=livro.id)
       print(f"Retrieved Livro: {livro}")

       updated_livro = update_livro(db, livro_id=livro.id, titulo="O Hobbit")
       print(f"Updated Livro: {updated_livro}")

       all_livros = get_all_livros(db)
       print(f"All Livros: {all_livros}")

       delete_livro(db, livro_id=livro.id)
       print(f"Deleted Livro: {livro.id}")

       # Operações CRUD para Resumos
       resumo = create_resumo(db, idusuario=user.id, idlivro=livro.id, resumo="Resumo do livro", paginasLidas=100)
       print(f"Created Resumo: {resumo}")

       resumo = get_resumo(db, resumo_id=resumo.id)
       print(f"Retrieved Resumo: {resumo}")

       updated_resumo = update_resumo(db, resumo_id=resumo.id, resumo="Resumo do livro atualizado", paginasLidas=150)
       print(f"Updated Resumo: {updated_resumo}")

       all_resumos = get_all_resumos(db)
       print(f"All Resumos: {all_resumos}")

       delete_resumo(db, resumo_id=resumo.id)
       print(f"Deleted Resumo: {resumo.id}")

   finally:
       db.close()

if __name__ == "__main__":
   run_crud_operations()  # Run CRUD operations
