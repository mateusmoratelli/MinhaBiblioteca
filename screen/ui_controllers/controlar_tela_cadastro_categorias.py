from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_cadastro_categorias as uiCateg
import database.crud.categoria as _crudCateg
import database.db_setup as dbSetup



class CadastroCategoria(uiCateg.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()  
        self.editar = False
        self.iniciarTela()
        self.defineAcoesBotoes()
        self.carregarListaCategorias()
        self.valoresIniciais()
    

    def iniciarTela(self):
        self.ui = uiCateg.Ui_Form()
        self.ui.setupUi(self)
    

    def defineAcoesBotoes(self):
        self.ui.btExcluirCategoria.clicked.connect(self.acaoExcluirCategoria)
        self.ui.btSalvarCategoria.clicked.connect(self.acaoSalvarGenero)
        self.ui.lstCategorias.clicked.connect(self.acaoPegarItemSelcionado)


    def valoresIniciais(self):
        self.ui.lbStatus.setText("")


    def carregarListaCategorias(self):
        self.textoItem = "" # para não encontrar nada na pesquisa
        self.ui.txtCategoria.setText("")
        self.ui.lstCategorias.clear()
        self.ui.itemSelected = False
        # busca na base de dados
        lst = _crudCateg.get_all_categoria(self.dbsql, 0, 999999)
        # print(lst)
        for i in lst:
            self.ui.lstCategorias.addItem(i.categoria)


    def acaoPegarItemSelcionado(self):
        item = self.ui.lstCategorias.currentItem()
        if item is not None:
            # Pega o texto do item selecionado
            self.textoItem = item.text()
            self.ui.txtCategoria.setText(self.textoItem)
            self.ui.itemSelected = True
        else:
            self.textoItem = ""


    def acaoExcluirCategoria(self):
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
                id = _crudCateg.search_categoria_by_name(self.dbsql, self.textoItem)[0].id
                deleted = _crudCateg.delete_categoria(self.dbsql, id)
                print(f"\nItem {deleted} deletado com sucesso.\n")
                self.carregarListaCategorias()
                self.ui.lbStatus.setText("A categoria foi exluída.")


    def acaoSalvarGenero(self):
        nomeNovoCategoria = str(self.ui.txtCategoria.text())
        self.ui.lbStatus.setText("")
        dbGenero = _crudCateg.get_categoria_by_name(self.dbsql, self.textoItem)
 
        if nomeNovoCategoria != "": 
            if dbGenero.__len__() == 0:
                listaSalva = _crudCateg.create_categoria(self.dbsql, nomeNovoCategoria)
            else:
                listaSalva = _crudCateg.update_categoria(self.dbsql, dbGenero[0].id,  nomeNovoCategoria )
            self.ui.lbStatus.setText("A categoria foi salvo com sucesso.")
            self.carregarListaCategorias()
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não permitido campo em branco. ")

        
