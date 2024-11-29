from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_main as uiMain
import screen.ui_controllers.controlar_tela_cadastro_genero as ctrlCadastro
import screen.ui_controllers.controlar_tela_cadastro_livros as ctrlLivros
import screen.ui_controllers.controlar_tela_cadastro_usuarios as ctrlUsuarios
import screen.ui_controllers.controlar_tela_sobre_sistema as ctrlSobre
from globais import *


class TelaMain():
    def __init__(self):
        self.iniciarAplicacao()
        self.defineFuncoesMenu()
        self.defineFuncoesBotoes()
        self.acaoLimparCampos()
        sys.exit(self.app.exec_())



    def iniciarAplicacao(self):
        self.app = uiMain.QtWidgets.QApplication(sys.argv)  # define o app
        self.telaMain = uiMain.QtWidgets.QMainWindow()      # define a tela Main
        self.ui = uiMain.Ui_MainWindow()                    # nomeia como self.ui a tela Main
        self.ui.setupUi(self.telaMain)                      # configura a tela inicial
        self.telaMain.show()
        self.ui.statusbar.showMessage(f"Bem vindo ao Programa: {APP}, Versão: {VERSION}-{RELEASED} feito por {BY}", 5000)



    def defineFuncoesMenu(self):
        self.ui.menuNovoLivro.triggered.connect(self.acaoNovoLivro)
        self.ui.menuCadatrarGenero.triggered.connect(self.acaoNovoGeneroLivro)
        self.ui.menuCadastrarUsuario.triggered.connect(self.acaoCadastroUsuarios)
        self.ui.menuSobrePrograma.triggered.connect(self.acaoAbrirTelaSobreSistema)



    def defineFuncoesBotoes(self):
        self.ui.btBuscarLivros
        self.ui.btLerResumo.clicked.connect(self.acaoLerResumo)
        self.ui.btEditarLivro.clicked.connect(self.acaoEditarLivro)
        self.ui.btAbrirPDF.clicked.connect(self.acaoAbrirPdf)
        self.ui.btNovoLivro.clicked.connect(self.acaoNovoLivro)



    def acaoLimparCampos(self):
        print("Limpando  campos")
        self.ui.lbTituloLivro.setText("")
        self.ui.lbAutor.setText("")
        self.ui.lbEditora.setText("")
        self.ui.lbGenero.setText("")
        self.ui.lbIsbn.setText("")
        self.ui.lbAnoPublicacao.setText("")
        self.ui.lbPDF.setText("")
        self.ui.lbPaginas.setText("")
        self.ui.lbPaginasLidas.setText("")
        self.ui.lbClassificacao.setText("")
        self.ui.txtSinopse.setText("")
        pixmap = QtGui.QPixmap("resources/img/capa_programa_principal.png")     # caminho da imagem 
        self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
        self.ui.lbCapa.setScaledContents(True)                                  # Ajusta a imagem para ocupar todo o espaço do QLabel        



    def acaoNovoLivro(self):
        print("menu novo livro")
        self.ui.statusbar.showMessage(f"Cadastrar novo livro", 3000)
        self.telaLivro = ctrlLivros.CadastrarLivro()
        self.telaLivro.show()
    


    def acaoNovoGeneroLivro(self):
        print("menu novo gênero de livro")
        self.ui.statusbar.showMessage(f"Cadastrar nova categoria", 3000)
        self.telaCateg = ctrlCadastro.CadastroCategoria()
        self.telaCateg.show()


    
    def acaoCadastroUsuarios(self):
        self.ui.statusbar.showMessage("Cadastrar Usuários", 3000)
        self.telaUsuario = ctrlUsuarios.CadastrarUsuario()
        self.telaUsuario.show()



    def acaoAbrirTelaSobreSistema(self):
        self.ui.statusbar.showMessage("Sobre o sistema", 3000)
        self.telaSobreSistema = ctrlSobre.SobreSistema()
        self.telaSobreSistema.show()

    

    def acaoLerResumo(self):
        print("Ler resumo do livro")



    def acaoEditarLivro(Self):
        print("Editar Livro")



    def acaoAbrirPdf(self):
        print("Abrir pdf ")
    


 
    

