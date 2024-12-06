from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_resumo_livro as scrResumo
from globais import *

import database.crud.resumo as crudResumo
import database.db_setup as dbSetup
import database.crud.usuario as crudUsuario

class Resumo(scrResumo.QtWidgets.QWidget):
    def __init__(self, idLivro:int, tituloLivro:str):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()
        self.idLivro = idLivro
        self.tituloLivro = tituloLivro
        self.iniciarTela()
        self.preencheInformacoes()
        self.definirAcoesObjetos()
        self.acaoCarregarListaUsuarios()
        self.acaoBuscarResumosUsuario()

    def iniciarTela(self):
        self.ui = scrResumo.Ui_Form()
        self.ui.setupUi(self)
        self.ui.lbTituloLivro.setText(self.tituloLivro)


    def preencheInformacoes(self):
        pass
        
    
    def definirAcoesObjetos(self):
        self.ui.btBuscarResumos.clicked.connect(self.acaoCarregarListaResumos)
        self.ui.btExcluir.clicked.connect(self.acaoExcluirResumo)
        self.ui.btSalvar.clicked.connect(self.acaoSalvarResumo)


    def acaoCarregarListaResumos(self):
        pass



    def acaoCarregarListaUsuarios(self):
        # limpando o campo
        self.ui.cbUsuario.clear()

        # preenchendo dados. 
        lstUser = crudUsuario.get_users(self.dbsql,0, 999999)
        for i in lstUser: 
            self.ui.cbUsuario.addItem(i.nome)
        


    def acaoBuscarResumosUsuario(self):
        # limpando os campos
        self.ui.txtResumo.setText("")
        self.ui.txtTituloResumo.setText("")
        self.ui.lstResumos.clear()
        
        # preenchendo as informações. 
        usuario = self.ui.cbUsuario.currentText()
        lstResumos = crudResumo.get_resumo_livro(self.dbsql, self.idLivro, usuario)
        for i in lstResumos:
            self.ui.lstResumos.addItem(i.tituloResumo)



    def acaoSalvarResumo(self):
        usuario = self.ui.cbUsuario.currentText()
        resumo = self.ui.txtResumo.toPlainText()
        tituloResumo = self.ui.txtTituloResumo.text()
        gravou = crudResumo.create_resumo(self.dbsql, usuario, self.idLivro, tituloResumo, resumo)
        print(gravou)
        self.acaoBuscarResumosUsuario()


    def acaoExcluirResumo(self):
        pass



    def acaoMontarHTML(self):
        pass

 
    


 

        