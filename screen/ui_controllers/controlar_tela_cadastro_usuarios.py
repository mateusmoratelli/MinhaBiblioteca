from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_cadastro_usuarios as uiUser
import database.db_setup as dbSetup
import database.crud.usuario as _crudUser


class CadastrarUsuario(uiUser.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.dbsql = dbSetup.SessionLocal()  
        self.iniciarTela()
        self.defineAcoesBotoes()
        self.carregaListaUsuarios()



    def iniciarTela(self):
        self.ui = uiUser.Ui_Form()
        self.ui.setupUi(self)
    


    def defineAcoesBotoes(self):
        self.ui.btExcluirUsuario.clicked.connect(self.acaoExcluirUsuario)
        self.ui.btSalvarUsuario.clicked.connect(self.acaoSalvarUsuario)
        self.ui.lstUsuarios.clicked.connect(self.acaoPegarItemSelcionado)
    


    def carregaListaUsuarios(self):
        self.textoItem = "" # para não encontrar nada na pesquisa
        self.ui.txtUsuario.setText("")
        self.ui.lstUsuarios.clear()
        self.itemSelected = False
        
        # busca na base de dados
        lst = _crudUser.get_users(self.dbsql, 0, 999999)
        print(lst)
        for i in lst:
            print(i)
            self.ui.lstUsuarios.addItem(i.nome)



    def acaoPegarItemSelcionado(self):
        item = self.ui.lstUsuarios.currentItem()
        if item is not None:
            # Pega o texto do item selecionado
            self.textoItem = item.text()
            self.ui.txtUsuario.setText(self.textoItem)
            self.itemSelected = True
        else:
            self.textoItem = ""


    def acaoExcluirUsuario(self):
        if self.itemSelected:
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
                id = _crudUser.get_user_by_name(self.dbsql, self.textoItem).id
                deleted = _crudUser.delete_user(self.dbsql, id)
                print(f"\nItem {deleted} deletado com sucesso.\n")
                self.carregaListaUsuarios()



    def acaoSalvarUsuario(self):
        nomeNovoUsuario = str(self.ui.txtUsuario.text())
        dbUsuarios = _crudUser.get_user_by_name(self.dbsql, self.textoItem)

        if nomeNovoUsuario != "": 
            if dbUsuarios == None:
                listaSalva = _crudUser.create_user(self.dbsql, nomeNovoUsuario)
            else:
                listaSalva = _crudUser.update_user(self.dbsql, dbUsuarios.id,  nomeNovoUsuario )
            print(f"|\nO Usuário foi salvo com sucesso no banco de dados:  {listaSalva}\n")
            self.carregaListaUsuarios()
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não permitido campo em branco. ")

        