from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_cadastro_usuarios as uiUser



class CadastrarUsuario(uiUser.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarTela()
        self.defineBotoes()

    def iniciarTela(self):
        self.ui = uiUser.Ui_Form()
        self.ui.setupUi(self)
    
    def defineBotoes(self):
        self.ui.btEditarUsuario.clicked.connect(self.acaoEditarUsuario)
        self.ui.btExcluirUsuario.clicked.connect(self.acaoExcluirUsuario)
        self.ui.btSalvarUsuario.clicked.connect(self.acaoSalvarUsuario)

    def acaoEditarUsuario(self):
        print("Editar usuário")

    def acaoExcluirUsuario(self):
        print("Excluir usuário")

    def acaoSalvarUsuario(self):
        print("Salvar usuário")

        