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
        self.ui.menuCadatrarTema.triggered.connect(self.acaoNovoTema)
        self.ui.menuCadastrarUsuario.triggered.connect(self.acaoCadastroUsuarios)
        self.ui.menuSobrePrograma.triggered.connect(self.acaoAbrirTelaSobreSistema)



    def defineFuncoesBotoes(self):
        self.ui.btBuscarLivros.clicked.connect(self.acaoBuscarLivros)
        self.ui.btLerResumo.clicked.connect(self.acaoLerResumo)
        self.ui.btEditarLivro.clicked.connect(self.acaoEditarLivro)
        self.ui.btAbrirPDF.clicked.connect(self.acaoAbrirPdf)
        self.ui.btNovoLivro.clicked.connect(self.acaoNovoLivro)
        self.ui.lstLivros.clicked.connect(self.acaoPegarItemSelecionado)
        # campo de pesquisa 
        self.ui.txtBuscar.returnPressed.connect(self.acaoBuscarLivros)



    def acaoBuscarLivros(self):
        print("buscar livros no banco de dados.")
        self.ui.lstLivros.clear()

        txtBuscar = self.ui.txtBuscar.text()
        lst = _crudLivros.get_livros_by_partial_titulo(self.dbsql, txtBuscar,0, 999999)
        totalLivros = lst.__len__()
        for i in lst: 
            self.ui.lstLivros.addItem(i.titulo)
        self.ui.statusbar.showMessage(f"Foram encontrados {totalLivros} livros")



    def acaoLimparCampos(self):
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
        



    def acaoNovoLivro(self):
        print("menu novo livro")
        self.ui.statusbar.showMessage(f"Cadastrar novo livro", 3000)
        self.telaLivro = ctrlLivros.CadastrarLivro(None, True)
        self.telaLivro.show()
    


    def acaoEditarLivro(self):
        print("menu novo livro")
        if  int(self.ui.lbID.text()) != 0:
            idLivro = int(self.ui.lbID.text())
            self.ui.statusbar.showMessage(f"Editar livro: {idLivro}", 3000)
            self.telaLivro = ctrlLivros.CadastrarLivro(idLivro, False)
            self.telaLivro.show()
        else: 
            self.ui.statusbar.showMessage("Selecione um livro!", 5000)



    def acaoPegarItemSelecionado(self):
        livroMarcado = self.ui.lstLivros.currentItem().text()
        if livroMarcado is not None:
            dbLivros = _crudLivros.get_livro_by_titulo(self.dbsql, livroMarcado)
            print(dbLivros)   
            self.ui.lbTituloLivro.setText(dbLivros.titulo)
            self.ui.lbAutor.setText(dbLivros.autor)
            self.ui.lbEditora.setText(dbLivros.editora)
            self.ui.lbTema.setText(dbLivros.tema)
            self.ui.lbIsbn.setText(dbLivros.isbn)
            self.ui.lbAnoPublicacao.setText(str(dbLivros.ano_publicacao))
            
            self.ui.lbPaginas.setText(str(dbLivros.paginas))
            # self.ui.lbPaginasLidas.setText(dbLivros.)
            self.ui.lbClassificacao.setText(str(dbLivros.classficacao))
            self.ui.txtSinopse.setText(dbLivros.sinopse)
            pixmap = QtGui.QPixmap(dbLivros.capa)     # caminho da imagem 
            self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)    
            self.ui.lbID.setText(str(dbLivros.id))     

            # verifica se exise PDF 
            if  dbLivros.pdf != "":
                self.ui.btAbrirPDF.setEnabled(True)
                self.ui.lbPDF.setText("SIM")
                self.pdf = dbLivros.pdf
            else:
                self.ui.btAbrirPDF.setEnabled(False)
                self.ui.lbPDF.setText("NÃO")

            # verifica a classificação
            estrelas = "⭐" * int(dbLivros.classficacao)
            self.ui.lbClassificacao.setText(str(estrelas))


    def acaoNovoTema(self):
        print("menu novo gênero de livro")
        self.ui.statusbar.showMessage(f"Cadastrar novo tema", 3000)
        self.telaTema = ctrlTemas.CadastrarTemas()
        self.telaTema.show()


    
    def acaoCadastroUsuarios(self):
        self.ui.statusbar.showMessage("Cadastrar Usuários", 3000)
        self.telaUsuario = ctrlUsuarios.CadastrarUsuario()
        self.telaUsuario.show()



    def acaoAbrirTelaSobreSistema(self):
        self.ui.statusbar.showMessage("Sobre o sistema", 3000)
        self.telaSobreSistema = ctrlSobre.SobreSistema()
        self.telaSobreSistema.show()

    

    def acaoLerResumo(self):
        self.ui.statusbar.showMessage("Carregando resumos", 3000)
        idLivro = self.ui.lbID.text()
        tituloLivro = self.ui.lbTituloLivro.text()
        autor = self.ui.lbAutor.text()
        self.telaResumo = ctrlResumo.Resumo(idLivro, tituloLivro)
        self.telaResumo.show()



    def acaoAbrirPdf(self):
        self.ui.statusbar.showMessage(f"Abrindo PDF: {self.pdf}", 8000)
        fm.FileManager().abrir_pdf(self.pdf)
    


   