from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_main as uiMain
import screen.ui_controllers.controlar_tela_cadastro_genero as ctrlCadastro
import screen.ui_controllers.controlar_tela_cadastro_livros as ctrlLivros
import screen.ui_controllers.controlar_tela_cadastro_usuarios as ctrlUsuarios
import screen.ui_controllers.controlar_tela_sobre_sistema as ctrlSobre
from contantes import *


class TelaMain():
    def __init__(self):
        self.iniciarAplicacao()
        self.defineFuncoesMenu()
        self.defineFuncoesBotoes()
        self.limparCampos()
        sys.exit(self.app.exec_())


    def iniciarAplicacao(self):
        self.app = uiMain.QtWidgets.QApplication(sys.argv)  # define o app
        self.telaMain = uiMain.QtWidgets.QMainWindow()      # define a tela Main
        self.ui = uiMain.Ui_MainWindow()                    # nomeia como self.ui a tela Main
        self.ui.setupUi(self.telaMain)                      # configura a tela inicial
        self.telaMain.show()
        self.ui.statusbar.showMessage(f"Bem vindo ao Programa: {APP}, Versão: {VERSION}-{RELEASED} feito por {BY}", 5000)


    def defineFuncoesMenu(self):
        self.ui.menuNovoLivro.triggered.connect(self.novoLivro)
        self.ui.menuCadatrarGenero.triggered.connect(self.novoGeneroLivro)
        self.ui.menuCadastrarUsuario.triggered.connect(self.cadastroUsuarios)
        self.ui.menuSobrePrograma.triggered.connect(self.acaoAbrirTelaSobreSistema)


    def defineFuncoesBotoes(self):
        self.ui.btLerResumo.clicked.connect(self.lerResumo)
        self.ui.btEditarLivro.clicked.connect(self.editarLivro)
        self.ui.btAbrirPDF.clicked.connect(self.abrirPdf)
        self.ui.btNovoLivro.clicked.connect(self.novoLivro)


    def novoLivro(self):
        print("menu novo livro")
        self.ui.statusbar.showMessage(f"Cadastrar novo livro", 3000)
        self.telaLivro = ctrlLivros.CadastrarLivro()
        self.telaLivro.show()
    

    def novoGeneroLivro(self):
        print("menu novo gênero de livro")
        self.ui.statusbar.showMessage(f"Cadastrar nova categoria", 3000)
        self.telaCateg = ctrlCadastro.CadastroCategoria()
        self.telaCateg.show()

    
    def cadastroUsuarios(self):
        self.ui.statusbar.showMessage("Cadastrar Usuários", 3000)
        self.telaUsuario = ctrlUsuarios.CadastrarUsuario()
        self.telaUsuario.show()

    def acaoAbrirTelaSobreSistema(self):
        self.ui.statusbar.showMessage("Sobre o sistema", 3000)
        self.telaSobreSistema = ctrlSobre.SobreSistema()
        self.telaSobreSistema.show()

    
    def lerResumo(self):
        print("Ler resumo do livro")


    def editarLivro(Self):
        print("Editar Livro")


    def abrirPdf(self):
        print("Abrir pdf ")
    
    def limparCampos(self):
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
    

