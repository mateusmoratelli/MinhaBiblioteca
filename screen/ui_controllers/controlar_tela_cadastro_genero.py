from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_cadastro_genero as uiCateg



class CadastroCategoria(uiCateg.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarTela()
        self.defineBotoes()

    def iniciarTela(self):
        self.ui = uiCateg.Ui_Form()
        self.ui.setupUi(self)
    
    def defineBotoes(self):
        self.ui.btEditarGenero.clicked.connect(self.acaoEditarGenero)
        self.ui.btExcluirGenero.clicked.connect(self.acaoExcluirGenero)
        self.ui.btSalvarGenero.clicked.connect(self.acaoSalvarGenero)

    def acaoEditarGenero(self):
        print("Editar gênero")

    def acaoExcluirGenero(self):
        print("Excluir gênero")

    def acaoSalvarGenero(self):
        print("Salvar gênero")

        
