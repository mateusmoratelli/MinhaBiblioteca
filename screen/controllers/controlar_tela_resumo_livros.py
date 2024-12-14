from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.generated.screen_resumo_livro as scrResumo
from globais import *

import database.crud.resumo as crudResumo
import database.db_setup as dbSetup
import database.crud.usuario as crudUsuario
import database.crud.livros as crud_livro

class Resumo(scrResumo.QtWidgets.QWidget):
    def __init__(self, idLivro:int, tituloLivro:str):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()
        self.idLivro = idLivro
        self.tituloLivro = tituloLivro
        self.lstIdResumo = []
        self.idResumoDb = -1
        self.html = ""
        self.iniciarTela()
        self.definirAcoesObjetos()
        self.acaoCarregarListaUsuarios()
        self.acaoCarregarListaResumos()



    def iniciarTela(self):
        self.ui = scrResumo.Ui_Form()
        self.ui.setupUi(self)
        self.ui.lbTituloLivro.setText(self.tituloLivro)
        self.ui.lbStatus.setText("")



    def definirAcoesObjetos(self):
        self.ui.btBuscarResumos.clicked.connect(self.acaoCarregarListaResumos)
        self.ui.btExcluir.clicked.connect(self.acaoExcluirResumo)
        self.ui.btSalvar.clicked.connect(self.acaoSalvarResumo)
        self.ui.lstResumos.clicked.connect(self.acaoItemListaClicado)



    def acaoCarregarListaUsuarios(self):
        # limpando o campo
        self.ui.cbUsuario.clear()

        # preenchendo dados. 
        lstUser = crudUsuario.get_users(self.dbsql,0, 999999)
        for i in lstUser: 
            self.ui.cbUsuario.addItem(i.nome)
        


    def acaoCarregarListaResumos(self):
        # limpando os campos
        self.ui.txtResumo.setText("")
        self.ui.txtTituloResumo.setText("")
        self.ui.lstResumos.clear()
        self.lstIdResumo.clear()
        self.html = ""
        
        # preenchendo as informações. 
        usuario = self.ui.cbUsuario.currentText()
        lstResumosDB = crudResumo.get_resumo_livro(self.dbsql, self.idLivro, usuario)
        for i in lstResumosDB:
            self.ui.lstResumos.addItem(i.tituloResumo)
            self.lstIdResumo.append(i.id)

            # registrar HTML
            self.html += f"<h2 style=\"color: blue;\">{i.tituloResumo}</h2> <br> {i.resumo} <hr>"
        print(f"Lista dos IDs {self.lstIdResumo}")
        self.acaoMontarHTML()


    def acaoSalvarResumo(self):
        usuario = self.ui.cbUsuario.currentText()
        resumo = self.ui.txtResumo.toPlainText()
        tituloResumo = self.ui.txtTituloResumo.text()
        self.idResumoDb = -1
        gravou = crudResumo.create_resumo(self.dbsql, usuario, self.idLivro, tituloResumo, resumo)
        print(gravou)
        self.acaoCarregarListaResumos()



    def acaoItemListaClicado(self):
        indexLista = self.ui.lstResumos.currentRow()
        self.idResumoDb = self.lstIdResumo[indexLista]
        print(f"\nIndex selecionado na lista {indexLista}, - ID do banco de dados {self.idResumoDb}\n")

        # buscar resumo no banco de dados. 
        resumoDB = crudResumo.get_resumo_livro_by_id(self.dbsql, self.idResumoDb)
        if resumoDB.__len__() > 0:
            self.ui.txtTituloResumo.setText(resumoDB[0].tituloResumo)
            self.ui.txtResumo.setText(resumoDB[0].resumo)



    def acaoExcluirResumo(self):
        if self.idResumoDb >= 0: 
            item = self.ui.txtTituloResumo.text()
            respostaBotao = QtWidgets.QMessageBox.question(
                self,
                "Confirmar Exclusão",
                f"Tem certeza de que deseja excluir '{item}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
            # Verifica a resposta do usuário
            if respostaBotao == QtWidgets.QMessageBox.Yes:
                deleted = crudResumo.delete_resumo(self.dbsql, self.idResumoDb)
                print(f"\nItem {deleted}, deletado com sucesso.")
                self.acaoCarregarListaResumos()



    def acaoMontarHTML(self):
        livro_db = crud_livro.get_livro_by_id(self.dbsql, self.idLivro)
        html = f"""
            <h1>{self.tituloLivro}</h1>
            <h4>Autor: </h4> 
            <br>{livro_db.autor}<br> 
            <HR>
            <img src=\"{livro_db.capa}\" alt=\"Imagem de um computador\" style=\"height: 100px; width: 100px;\">
</body>
            {self.html}
        """
        print(html)
        self.ui.textBrowser.setHtml(html)