import test.user_crud_test as _myCrud

VERSION = "1.0.0"
APP = "TESTE DE TELAS "
REV = "2024.11.13"
BY = "MATEUS MORATELLI"


if __name__ == "__main__":
    print(f"""
          
    ###############################################################      
        BEM VINDO AO PROGRAMA
        {APP}  
        VERSÃO: {VERSION} - Relesed: {REV}
        by: {BY}
    ###############################################################
        
    """)
    _myCrud.run_crud_operations()

