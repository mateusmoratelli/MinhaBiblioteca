import sys
from argparse import Action
from PyQt5.QtWidgets import  QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore

from globais import * 
import screen.generated.screen_cadastro_livros as uiLivros
import database.crud.livros as _crudLivros
import database.crud.tema as crud_temas
import database.db_setup as dbSetup
import utils.files_manager as fileMana
import utils.funcoes_globais as _utis
from pathlib import Path # para pegar dados do arquivo. 


class CadastrarLivro(uiLivros.QtWidgets.QWidget):  
    def __init__(self, id_livro:int, eh_livro_novo:bool):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()
        self.id_livro = id_livro
        self.eh_livro_novo = eh_livro_novo
        self.capa = "resources\img\capa_programa_principal.png"
        self.pdf = ""
        self.uuid = _utis.gerar_uuid()
        self.iniciar_tela()
        self.definir_acoes_botoes()
        self.acao_buscar_temas()
        self.informacoes_livro()



    def iniciar_tela(self):
        self.ui = uiLivros.Ui_Form()
        self.ui.setupUi(self)
        self.ui.lbStatus.setText("")



    def definir_acoes_botoes(self):
        self.ui.btAlterarCapa.clicked.connect(self.acao_adicionar_capa)
        self.ui.btEnviarPDF.clicked.connect(self.acao_enviar_pdf_pasta)
        self.ui.btExcluirLivro.clicked.connect(self.acao_excluir)
        self.ui.btSalvarLivro.clicked.connect(self.acao_salvar)
        


    def informacoes_livro(self):
        if self.eh_livro_novo == False: 
            db_livro = _crudLivros.get_livro_by_id(self.id_livro)
            print(db_livro)
            self.ui.txtLivro.setText(db_livro.titulo)
            self.ui.txtAutor.setText(db_livro.autor)
            self.ui.txtEditora.setText(db_livro.editora)
            self.ui.cbTema.setCurrentText(db_livro.tema)
            self.ui.txtIsbn.setText(db_livro.isbn)
            self.ui.txtPaginas.setText(db_livro.paginas)
            self.ui.txtAno.setText(db_livro.ano_publicacao)
            self.ui.sliderClassificacao.setValue(int(db_livro.classficacao))
            self.ui.txtSinopse.setText(db_livro.sinopse)
            self.capa = db_livro.capa
            pixmap = QtGui.QPixmap(self.capa)       # caminho da imagem
            self.ui.lbCapa.setPixmap(pixmap)        # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)



    def acao_salvar(self):
        livro = self.ui.txtLivro.text()
        autor = self.ui.txtAutor.text()
        editora = self.ui.txtEditora.text()
        tema = self.ui.cbTema.currentText()
        isbn = self.ui.txtIsbn.text()
        paginas = self.ui.txtPaginas.text()
        ano = self.ui.txtAno.text()
        classificacao = self.ui.sliderClassificacao.value()
        sinopse = self.ui.txtSinopse.toPlainText()
        livro_id = self.id_livro

        if self.eh_livro_novo:
            gravado = _crudLivros.create_livro(self.dbsql, livro, autor, editora, 
                                            tema, isbn, paginas, ano, self.capa,
                                            self.pdf, classificacao, sinopse)
        else: 
            gravado = _crudLivros.update_livro(self.dbsql, livro_id, livro, autor, editora, 
                                            tema, isbn, paginas, ano, self.capa,
                                            self.pdf, classificacao, sinopse)         

        self.ui.lbStatus.setText(f"Livro Gravado com sucesso, ID: {gravado.id} - {gravado.titulo}")
        print(f"\nLivro gravado com sucesso. {gravado}")


    def acao_buscar_temas(self):
        self.ui.cbTema.clear()
        lst_db = crud_temas.get_all_tema(0, 999999)
        for i in lst_db:
            self.ui.cbTema.addItem(i.tema)
            


    def acao_excluir(self):
        resposta = QtWidgets.QMessageBox.question(
                self,
                "Confirmar Exclusão",
                f"Tem certeza de que deseja excluir '{self.id_livro}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
        # Verifica a resposta do usuário
        if resposta == QtWidgets.QMessageBox.Yes:
            deleted = _crudLivros.delete_livro(self.dbsql, self.id_livro)
            print(deleted)
            self.close()


    def acao_adicionar_capa(self):
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
            self.ui.lbCapa.setPixmap(pixmap)      # Seta um pixmap
            self.ui.lbCapa.setScaledContents(True)
            self.ui.lbStatus.setText("Capa atualizada com sucesso.")
        else:
            self.ui.lbStatus.setText('Nenhuma imagem selecionada')

 
 
    def acao_enviar_pdf_pasta(self):
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