from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_cadastro_temas as uiTemas
import database.crud.tema as _crudTemas
import database.db_setup as dbSetup



class CadastrarTemas(uiTemas.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()  
        self.editar = False
        self.iniciarTela()
        self.defineAcoesBotoes()
        self.carregarListaTemas()
        self.valoresIniciais()
    

    def iniciarTela(self):
        self.ui = uiTemas.Ui_Form()
        self.ui.setupUi(self)
    

    def defineAcoesBotoes(self):
        self.ui.btExcluirTema.clicked.connect(self.acaoExcluirTema)
        self.ui.btSalvarTema.clicked.connect(self.acaoSalvarTema)
        self.ui.lstTemas.clicked.connect(self.acaoPegarItemSelcionado)


    def valoresIniciais(self):
        self.ui.lbStatus.setText("")


    def carregarListaTemas(self):
        self.textoItem = "" # para não encontrar nada na pesquisa
        self.ui.txtTema.setText("")
        self.ui.lstTemas.clear()
        self.ui.itemSelected = False
        # busca na base de dados
        lst = _crudTemas.get_all_tema(self.dbsql, 0, 999999)
        # print(lst)
        for i in lst:
            self.ui.lstTemas.addItem(i.tema)


    def acaoPegarItemSelcionado(self):
        item = self.ui.lstTemas.currentItem()
        if item is not None:
            # Pega o texto do item selecionado
            self.textoItem = item.text()
            self.ui.txtTema.setText(self.textoItem)
            self.ui.itemSelected = True
        else:
            self.textoItem = ""
        self.ui.lbStatus.setText(f"Item selecionado: {self.textoItem}")


    def acaoExcluirTema(self):
        self.ui.lbStatus.setText("")
        if self.ui.itemSelected:
            # Exibe uma mensagem de confirmação
            resposta = QtWidgets.QMessageBox.question(
                self,
                "Confirmar Exclusão",
                f"Tem certeza de que deseja excluir '{self.textoItem}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            # Verifica a resposta do usuário
            if resposta == QtWidgets.QMessageBox.Yes:
                # Remove o item selecionado
                id = _crudTemas.search_tema_by_name(self.dbsql, self.textoItem)[0].id
                deleted = _crudTemas.delete_tema(self.dbsql, id)
                print(f"\nItem {deleted} deletado com sucesso.\n")
                self.carregarListaTemas()
                self.ui.lbStatus.setText(f"O Tema '{deleted.tema}' foi excluído.")


    def acaoSalvarTema(self):
        nomeNovoTema = str(self.ui.txtTema.text())
        self.ui.lbStatus.setText("")
        dbTema = _crudTemas.get_tema_by_name(self.dbsql, self.textoItem)
 
        if nomeNovoTema != "": 
            if dbTema.__len__() == 0:
                listaSalva = _crudTemas.create_tema(self.dbsql, nomeNovoTema)
            else:
                listaSalva = _crudTemas.update_tema(self.dbsql, dbTema[0].id,  nomeNovoTema )
            self.carregarListaTemas()
            self.ui.lbStatus.setText(f"O tema foi salvo com sucesso. ID: {listaSalva.id}")
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não permitido campo em branco. ")

        
