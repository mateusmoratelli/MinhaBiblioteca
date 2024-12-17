""""""
import screen.controllers.controlar_tela_main as tela_main
from globais import * 
from utils.files_manager import FileManager as fm
 
if __name__ == "__main__":
    print(f"""
          
    ###############################################################      
        BEM VINDO AO PROGRAMA
        {APP}  
        VERSÃO: {VERSION} - Relesed: {RELEASED}
        by: {BY}
    ###############################################################
        
    """)

    # Verificar se a pasta existe caso não existe criar. 
    fm(PASTA_BASE).create_folder(PASTA_BASE)
    # testarCrud.run_crud_operations()
    tela_main.TelaMain()

