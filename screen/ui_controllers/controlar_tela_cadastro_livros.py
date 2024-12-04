from argparse import Action
from PyQt5.QtWidgets import  QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
import sys

from globais import * 
import screen.ui_generated.screen_cadastro_livros as uiLivros
import database.crud.livros as _crudLivros
import database.crud.tema as _crudTemas
import database.db_setup as dbSetup
import utils.files_manager as fileMana
import utils.funcoes_globais as _utis
from pathlib import Path # para pegar dados do arquivo. 


class CadastrarLivro(uiLivros.QtWidgets.QWidget):  
    def __init__(self, idLivro:int, ehLivroNovo:bool):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()
        self.idLivro = idLivro
        self.ehLivroNovo = ehLivroNovo
        self.capa = "resources\img\capa_programa_principal.png"
        self.pdf = ""
        self.uuid = _utis.gerarUUID()
        self.iniciarTela()
        self.defineBotoes()
        self.acaoBuscarTemas()
        self.informacoesLivro()



    def iniciarTela(self):
        self.ui = uiLivros.Ui_Form()
        self.ui.setupUi(self)
        self.ui.lbStatus.setText("")



    def defineBotoes(self):
        self.ui.btAlterarCapa.clicked.connect(self.acaoAdicionarCapa)
        self.ui.btEnviarPDF.clicked.connect(self.acaoEnviarPDF)
        self.ui.btExcluirLivro.clicked.connect(self.acaoExcluir)
        self.ui.btSalvarLivro.clicked.connect(self.acaoSalvar)
        


    def informacoesLivro(self):
        if self.ehLivroNovo == False: 
            dbLivro = _crudLivros.get_livro_by_id(self.dbsql, self.idLivro)
            print(dbLivro)
            self.ui.txtLivro.setText(dbLivro.titulo)
            self.ui.txtAutor.setText(dbLivro.autor)
            self.ui.txtEditora.setText(dbLivro.editora)
            self.ui.cbTema.setCurrentText(dbLivro.tema)
            self.ui.txtIsbn.setText(dbLivro.isbn)
            self.ui.txtPaginas.setText(dbLivro.paginas)
            self.ui.txtAno.setText(dbLivro.ano_publicacao)
            self.ui.sliderClassificacao.setValue(int(dbLivro.classficacao))
            self.ui.txtSinopse.setText(dbLivro.sinopse)
            self.capa = dbLivro.capa
            pixmap = QtGui.QPixmap(self.capa)     # caminho da imagem 
            self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)  




    def acaoSalvar(self):
        livro = self.ui.txtLivro.text()
        autor = self.ui.txtAutor.text()
        editora = self.ui.txtEditora.text()
        tema = self.ui.cbTema.currentText()
        isbn = self.ui.txtIsbn.text()
        paginas = self.ui.txtPaginas.text()
        ano = self.ui.txtAno.text()
        classificacao = self.ui.sliderClassificacao.value()
        sinopse = self.ui.txtSinopse.toPlainText()
        livroId = self.idLivro

        if self.ehLivroNovo:
            gravado = _crudLivros.create_livro(self.dbsql, livro, autor, editora, 
                                            tema, isbn, paginas, ano, self.capa, 
                                            self.pdf, classificacao, sinopse)
        else: 
            gravado = _crudLivros.update_livro(self.dbsql, livroId, livro, autor, editora, 
                                            tema, isbn, paginas, ano, self.capa, 
                                            self.pdf, classificacao, sinopse)            

        self.ui.lbStatus.setText(f"Livro Gravado com sucesso, ID: {gravado.id} - {gravado.titulo}")
        print(f"\nLivro gravado com sucesso. {gravado.id}")


    def acaoBuscarTemas(self):
        self.ui.cbTema.clear()
        lstDb = _crudTemas.get_all_tema(self.dbsql,0, 999999)
        for i in lstDb:
            self.ui.cbTema.addItem(i.tema)
            


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
            fileMana.FileManager(PASTA_BASE).copy_file(file_name, PASTA_BASE,  dest_file)

            self.capa = f"{PASTA_BASE}{dest_file}"
            pixmap = QtGui.QPixmap(self.capa)     # caminho da imagem 
            self.ui.lbCapa.setPixmap(pixmap)                                        # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)  
            self.ui.lbStatus.setText("Capa atualizada com sucesso.")
        else:
            self.ui.lbStatus.setText('Nenhuma imagem selecionada')

 
 
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
            fileMana.FileManager(PASTA_BASE).copy_file(file_name, PASTA_BASE,  dest_file)
            self.pdf = f"{PASTA_BASE}{dest_file}"
            self.ui.lbStatus.setText(f"PDF enviado com sucesso: {self.pdf}")