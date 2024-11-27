from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.screen_cadastro_livros as uiLivros



class CadastrarLivro(uiLivros.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarTela()
        self.defineBotoes()

    def iniciarTela(self):
        self.ui = uiLivros.Ui_Form()
        self.ui.setupUi(self)
    
    def defineBotoes(self):
        self.ui.btAlterarCapa.clicked.connect(self.acaoAdicionarCapa)
        self.ui.btEnviarPDF.clicked.connect(self.acaoEnviarPDF)
        self.ui.btExcluirLivro.clicked.connect(self.acaoExcluir)
        self.ui.btSalvarLivro.clicked.connect(self.acaoSalvar)

    def acaoSalvar(self):
        print("Botão salvar livro clicado")

    def acaoExcluir(self):
        print("Botão Excluir clicado")

    def acaoAdicionarCapa(self):
        print("Botão adicionar capa clicado")

    def acaoEnviarPDF(self):
        print("Enviar Livro em pdf")