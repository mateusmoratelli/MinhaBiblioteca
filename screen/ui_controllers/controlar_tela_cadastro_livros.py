from argparse import Action
from PyQt5.QtWidgets import  QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
import sys

from globais import * 
import screen.ui_generated.screen_cadastro_livros as uiLivros
import database.crud.livros as _crudLivros
import database.db_setup as dbSetup
import utils.files_manager as _fm
import utils.funcoes_globais as _utis
from pathlib import Path # para pegar dados do arquivo. 


class CadastrarLivro(uiLivros.QtWidgets.QWidget):  
    def __init__(self, tituloSelecionado:str, ehLivroNovo:bool):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()
        self.tituloSelecionado = tituloSelecionado
        self.ehLivroNovo = ehLivroNovo
        self.capa = "resources\img\capa_programa_principal.png"
        self.pdf = ""
        self.uuid = _utis.gerarUUID()
        self.iniciarTela()
        self.defineBotoes()



    def iniciarTela(self):
        self.ui = uiLivros.Ui_Form()
        self.ui.setupUi(self)



    def defineBotoes(self):
        self.ui.btAlterarCapa.clicked.connect(self.acaoAdicionarCapa)
        self.ui.btEnviarPDF.clicked.connect(self.acaoEnviarPDF)
        self.ui.btExcluirLivro.clicked.connect(self.acaoExcluir)
        self.ui.btSalvarLivro.clicked.connect(self.acaoSalvar)
        



    def acaoSalvar(self):
        livro = self.ui.txtLivro.text()
        autor = self.ui.txtAutor.text()
        editora = self.ui.txtEditora.text()
        genero = self.ui.cbGenero.currentText()
        isbn = self.ui.txtIsbn.text()
        paginas = self.ui.txtPaginas.text()
        ano = self.ui.txtAno.text()
        classificacao = self.ui.sliderClassificacao.value()
        sinopse = self.ui.txtSinopse.toPlainText()
        gravado = _crudLivros.create_livro(self.dbsql, livro, autor, editora, 
                                           genero, isbn, paginas, ano, self.capa, 
                                           self.pdf, classificacao, sinopse)
        
        print(f"\nLivro gravado com sucesso. {gravado}")

 

    def acaoExcluir(self):
        print("Botão Excluir clicado")



    def acaoAdicionarCapa(self):
        # Abre o explorador de arquivos para escolher uma imagem
        file_name, _ = QFileDialog.getOpenFileName(self, "Escolher Imagem", "", 
                                                   "Imagens (*.png *.jpg *.jpeg *.bmp *.gif);;Todos os Arquivos (*.*)")
        if file_name:  # Verifica se o usuário selecionou algum arquivo
            # Define o texto do QLabel como o caminho da imagem
            # novo novo do arquivo
 
            nome_arquivo_com_extensao = Path(file_name).name
            dest_file = f"{self.uuid}_{nome_arquivo_com_extensao}"
            # copiar para pasta
            _fm.FileManager(PASTA_BASE).copy_file(file_name, PASTA_BASE,  dest_file)

            self.capa = f"{PASTA_BASE}{dest_file}"
            pixmap = QtGui.QPixmap(self.capa)     # caminho da imagem 
            self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)  
            
        else:
            self.ui.lbCapa.setText('Nenhuma imagem selecionada')

 
 
    def acaoEnviarPDF(self):
        # Abre o explorador de arquivos para escolher uma imagem
        file_name, _ = QFileDialog.getOpenFileName(self, "Escolher PDF", "", 
                                                   "PDF (*pdf );;Todos os Arquivos (*.*)")
        if file_name:  # Verifica se o usuário selecionou algum arquivo
            # Define o texto do QLabel como o caminho da imagem
            # novo novo do arquivo
 
            nome_arquivo_com_extensao = Path(file_name).name
            dest_file = f"{self.uuid}_{nome_arquivo_com_extensao}"
            # copiar para pasta
            _fm.FileManager(PASTA_BASE).copy_file(file_name, PASTA_BASE,  dest_file)
            self.pdf = f"{PASTA_BASE}{dest_file}"