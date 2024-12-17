from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

# importar telas 
import screen.generated.screen_main as uiMain
import screen.controllers.controlar_tela_cadastro_temas as ctrlTemas
import screen.controllers.controlar_tela_cadastro_livros as ctrlLivros
import screen.controllers.controlar_tela_cadastro_usuarios as ctrlUsuarios
import screen.controllers.controlar_tela_sobre_sistema as ctrlSobre
import screen.controllers.controlar_tela_resumo_livros as ctrlResumo

# importar banco de dados
import database.crud.livros as _crudLivros
import database.db_setup as dbSetup

# importar funções uteis
from globais import *
import utils.files_manager as fm



class TelaMain():
    def __init__(self):
        # self.dbsql = dbSetup.SessionLocal()
        self.iniciar_aplicacao()
        self.define_funcoes_menu()
        self.define_funcoes_botoes()
        self.acao_limpar_campos()
        self.acao_buscar_livros()
        sys.exit(self.app.exec_())



    def iniciar_aplicacao(self):
        self.app = uiMain.QtWidgets.QApplication(sys.argv)  # define o app
        self.tela_main = uiMain.QtWidgets.QMainWindow()      # define a tela Main
        self.ui = uiMain.Ui_MainWindow()                    # nomeia como self.ui a tela Main
        self.ui.setupUi(self.tela_main)                      # configura a tela inicial
        self.tela_main.show()
        self.ui.statusbar.showMessage(f"Bem vindo ao Programa: {APP}, Versão: {VERSION}-{RELEASED} feito por {BY}", 5000)



    def define_funcoes_menu(self):
        self.ui.menuNovoLivro.triggered.connect(self.acao_novo_livro)
        self.ui.menuCadatrarTema.triggered.connect(self.acao_novo_tema)
        self.ui.menuCadastrarUsuario.triggered.connect(self.acao_cadastro_usuarios)
        self.ui.menuSobrePrograma.triggered.connect(self.acao_abrir_tela_sobre_sistema)



    def define_funcoes_botoes(self):
        self.ui.btBuscarLivros.clicked.connect(self.acao_buscar_livros)
        self.ui.btLerResumo.clicked.connect(self.acao_ler_resumo)
        self.ui.btEditarLivro.clicked.connect(self.acao_editar_livro)
        self.ui.btAbrirPDF.clicked.connect(self.acao_abri_pdf)
        self.ui.btNovoLivro.clicked.connect(self.acao_novo_livro)
        self.ui.lstLivros.clicked.connect(self.acao_pegar_item_selecionado)
        # campo de pesquisa 
        self.ui.txtBuscar.returnPressed.connect(self.acao_buscar_livros)



    def acao_buscar_livros(self):
        print("buscar livros no banco de dados.")
        self.ui.lstLivros.clear()

        txt_buscar = self.ui.txtBuscar.text()
        lst = _crudLivros.get_livros_by_partial_titulo(txt_buscar, 0, 999999)
        total_livros = lst.__len__()
        for i in lst: 
            self.ui.lstLivros.addItem(i.titulo)
        self.ui.statusbar.showMessage(f"Foram encontrados {total_livros} livros")



    def acao_limpar_campos(self):
        print("Limpando  campos")
        self.ui.lbTituloLivro.setText("")
        self.ui.lbAutor.setText("")
        self.ui.lbEditora.setText("")
        self.ui.lbTema.setText("")
        self.ui.lbIsbn.setText("")
        self.ui.lbAnoPublicacao.setText("")
        self.ui.lbPDF.setText("")
        self.ui.lbPaginas.setText("")
        self.ui.lbPaginasLidas.setText("")
        self.ui.lbClassificacao.setText("")
        self.ui.txtSinopse.setText("")
        pixmap = QtGui.QPixmap("resources/img/capa_programa_principal.png")     # caminho da imagem 
        self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
        self.ui.lbCapa.setScaledContents(True)  
        self.ui.lbID.setText("0000")
        



    def acao_novo_livro(self):
        print("menu novo livro")
        self.ui.statusbar.showMessage("Cadastrar novo livro", 3000)
        self.tela_livro = ctrlLivros.CadastrarLivro(None, True)
        self.tela_livro.show()
    


    def acao_editar_livro(self):
        print("menu novo livro")
        if  int(self.ui.lbID.text()) != 0:
            id_livro = int(self.ui.lbID.text())
            self.ui.statusbar.showMessage(f"Editar livro: {id_livro}", 3000)
            self.tela_livro = ctrlLivros.CadastrarLivro(id_livro, False)
            self.tela_livro.show()
        else: 
            self.ui.statusbar.showMessage("Selecione um livro!", 5000)



    def acao_pegar_item_selecionado(self):
        livro_marcado = self.ui.lstLivros.currentItem().text()
        if livro_marcado is not None:
            db_livro = _crudLivros.get_livro_by_titulo(livro_marcado)
            print(db_livro)   
            self.ui.lbTituloLivro.setText(db_livro.titulo)
            self.ui.lbAutor.setText(db_livro.autor)
            self.ui.lbEditora.setText(db_livro.editora)
            self.ui.lbTema.setText(db_livro.tema)
            self.ui.lbIsbn.setText(db_livro.isbn)
            self.ui.lbAnoPublicacao.setText(str(db_livro.ano_publicacao))
            
            self.ui.lbPaginas.setText(str(db_livro.paginas))
            # self.ui.lbPaginasLidas.setText(dbLivros.)
            self.ui.lbClassificacao.setText(str(db_livro.classficacao))
            self.ui.txtSinopse.setText(db_livro.sinopse)
            pixmap = QtGui.QPixmap(db_livro.capa)     # caminho da imagem 
            self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)    
            self.ui.lbID.setText(str(db_livro.id))     

            # verifica se exise PDF 
            if  db_livro.pdf != "":
                self.ui.btAbrirPDF.setEnabled(True)
                self.ui.lbPDF.setText("SIM")
                self.pdf = db_livro.pdf
            else:
                self.ui.btAbrirPDF.setEnabled(False)
                self.ui.lbPDF.setText("NÃO")

            # verifica a classificação
            estrelas = "⭐" * int(db_livro.classficacao)
            self.ui.lbClassificacao.setText(str(estrelas))


    def acao_novo_tema(self):
        print("menu novo gênero de livro")
        self.ui.statusbar.showMessage("Cadastrar novo tema", 3000)
        self.tela_tema = ctrlTemas.CadastrarTemas()
        self.tela_tema.show()


    
    def acao_cadastro_usuarios(self):
        self.ui.statusbar.showMessage("Cadastrar Usuários", 3000)
        self.tela_usuarios = ctrlUsuarios.CadastrarUsuario()
        self.tela_usuarios.show()



    def acao_abrir_tela_sobre_sistema(self):
        self.ui.statusbar.showMessage("Sobre o sistema", 3000)
        self.tela_sobre_sistema = ctrlSobre.SobreSistema()
        self.tela_sobre_sistema.show()

    

    def acao_ler_resumo(self):
        self.ui.statusbar.showMessage("Carregando resumos", 3000)
        id_livro = self.ui.lbID.text()
        titulo_livro = self.ui.lbTituloLivro.text()
        autor = self.ui.lbAutor.text()
        self.tela_resumo = ctrlResumo.Resumo(id_livro, titulo_livro)
        self.tela_resumo.show()



    def acao_abri_pdf(self):
        self.ui.statusbar.showMessage(f"Abrindo PDF: {self.pdf}", 8000)
        fm.FileManager().abrir_pdf(self.pdf)
    


   