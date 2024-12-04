# import test.user_crud_test as _myCrud
import screen.ui_controllers.controlar_tela_main as telaMain
from globais import * 
from utils.files_manager import FileManager as fileManeger
import test.debug_tema as dtema
# import test.user_crud_test as testarCrud
 
if __name__ == "__main__":
    print(f"""
          
    ###############################################################      
        BEM VINDO AO PROGRAMA
        {APP}  
        VERSÃO: {VERSION} - Relesed: {RELEASED}
        by: {BY}
    ###############################################################
        
    """)

    dtema.inicio()
    # Verificar se a pasta existe caso não existe criar. 
    fileManeger(PASTA_BASE).create_folder(PASTA_BASE)
    # testarCrud.run_crud_operations()
    telaMain.TelaMain()

