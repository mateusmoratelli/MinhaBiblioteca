from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_main as uiMain
import screen.ui_controllers.controlar_tela_cadastro_categorias as ctrlCategoria
import screen.ui_controllers.controlar_tela_cadastro_livros as ctrlLivros
import screen.ui_controllers.controlar_tela_cadastro_usuarios as ctrlUsuarios
import screen.ui_controllers.controlar_tela_sobre_sistema as ctrlSobre

import database.crud.livros as _crudLivros
import database.db_setup as dbSetup
from globais import *


class TelaMain():
    def __init__(self):
        self.dbsql = dbSetup.SessionLocal()
        self.iniciarAplicacao()
        self.defineFuncoesMenu()
        self.defineFuncoesBotoes()
        self.acaoLimparCampos()
        self.acaoBuscarLivros()
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
        self.ui.menuCadatrarCategorias.triggered.connect(self.acaoNovaCategoria)
        self.ui.menuCadastrarUsuario.triggered.connect(self.acaoCadastroUsuarios)
        self.ui.menuSobrePrograma.triggered.connect(self.acaoAbrirTelaSobreSistema)



    def defineFuncoesBotoes(self):
        self.ui.btAtualizar.clicked.connect(self.acaoBuscarLivros)
        self.ui.btBuscarLivros.clicked.connect(self.acaoBuscarLivros)
        self.ui.btLerResumo.clicked.connect(self.acaoLerResumo)
        self.ui.btEditarLivro.clicked.connect(self.acaoEditarLivro)
        self.ui.btAbrirPDF.clicked.connect(self.acaoAbrirPdf)
        self.ui.btNovoLivro.clicked.connect(self.acaoNovoLivro)
        self.ui.lstLivros.clicked.connect(self.acaoPegarItemSelecionado)



    def acaoBuscarLivros(self):
        print("buscar livros no banco de dados.")
        self.ui.lstLivros.clear()
        lst = _crudLivros.get_all_livros(self.dbsql, 0, 999999)
        for i in lst: 
            self.ui.lstLivros.addItem(i.titulo)



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
        self.ui.lbCapa.setScaledContents(True)  
        self.ui.lbID.setText("0000")
        
        

    def acaoPegarItemSelecionado(self):
        self.itemSelecionado = self.ui.lstLivros.currentItem()                                # Ajusta a imagem para ocupar todo o espaço do QLabel        



    def acaoNovoLivro(self):
        print("menu novo livro")
        self.ui.statusbar.showMessage(f"Cadastrar novo livro", 3000)
        self.telaLivro = ctrlLivros.CadastrarLivro("", False)
        self.telaLivro.show()
    


    def acaoPegarItemSelecionado(self):
        livroMarcado = self.ui.lstLivros.currentItem().text()
        if livroMarcado is not None:
            dbLivros = _crudLivros.get_livro_by_titulo(self.dbsql, livroMarcado)
            self.ui.lbTituloLivro.setText(dbLivros.titulo)
            self.ui.lbAutor.setText(dbLivros.autor)
            self.ui.lbEditora.setText(dbLivros.editora)
            self.ui.lbGenero.setText(dbLivros.genero)
            self.ui.lbIsbn.setText(dbLivros.isbn)
            self.ui.lbAnoPublicacao.setText(str(dbLivros.ano_publicacao))
            self.ui.lbPDF.setText(dbLivros.pdf)
            self.ui.lbPaginas.setText(str(dbLivros.paginas))
            # self.ui.lbPaginasLidas.setText(dbLivros.)
            self.ui.lbClassificacao.setText(str(dbLivros.classficacao))
            self.ui.txtSinopse.setText(dbLivros.sinopse)
            pixmap = QtGui.QPixmap(dbLivros.capa)     # caminho da imagem 
            self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)    
            self.ui.lbID.setText(str(dbLivros.id))     
            print(dbLivros)    

    def acaoNovaCategoria(self):
        print("menu novo gênero de livro")
        self.ui.statusbar.showMessage(f"Cadastrar nova categoria", 3000)
        self.telaCateg = ctrlCategoria.CadastroCategoria()
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
    


 
    

