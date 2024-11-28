from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_cadastro_genero as uiCateg
import database.crud.genero as _crudGenero
import database.db_setup as dbSetup



class CadastroCategoria(uiCateg.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()  
        self.editar = False
        self.iniciarTela()
        self.defineBotoes()
        self.carregarListaGenero()
    

    def iniciarTela(self):
        self.ui = uiCateg.Ui_Form()
        self.ui.setupUi(self)
    

    def defineBotoes(self):
        self.ui.btExcluirGenero.clicked.connect(self.acaoExcluirGenero)
        self.ui.btSalvarGenero.clicked.connect(self.acaoSalvarGenero)
        self.ui.lstGeneros.clicked.connect(self.acaoPegarItemSelcionado)


    def carregarListaGenero(self):
        self.textoItem = "1111111111111111111111111111111111111111111111111111" # para não encontrar nada na pesquisa
        self.ui.txtGenero.setText("")
        self.ui.lstGeneros.clear()
        self.ui.itemSelected = False
        # busca na base de dados
        lst = _crudGenero.get_all_genero(self.dbsql, 0, 999999)
        print(lst)
        for i in lst:
            print(i)
            self.ui.lstGeneros.addItem(i.genero)


    def acaoPegarItemSelcionado(self):
        item = self.ui.lstGeneros.currentItem()
        if item is not None:
            # Pega o texto do item selecionado
            self.textoItem = item.text()
            self.ui.txtGenero.setText(self.textoItem)
            self.ui.itemSelected = True
        else:
            self.textoItem = "1111111111111111111111111111111111111111111111111111"


    def acaoExcluirGenero(self):
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
                id = _crudGenero.search_genero_by_name(self.dbsql, self.textoItem)[0].id
                deleted = _crudGenero.delete_genero(self.dbsql, id)
                print(f"\nItem {deleted} deletado com sucesso.\n")
                self.carregarListaGenero()


    def acaoSalvarGenero(self):
        nomeNovoGenero = str(self.ui.txtGenero.text())
        dbGenero = _crudGenero.search_genero_by_name(self.dbsql, self.textoItem)
        jaCadastrado = dbGenero.__len__()

        if nomeNovoGenero != "": 
            if jaCadastrado == 0:
                listaSalva = _crudGenero.create_genero(self.dbsql, nomeNovoGenero)
            else:
                listaSalva = _crudGenero.update_genero(self.dbsql, dbGenero[0].id,  nomeNovoGenero )
            print(f"|\nO Gênero foi salvo com sucesso no banco de dados:  {listaSalva}\n")
    
            self.carregarListaGenero()
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não permitido campo em branco. ")

        
