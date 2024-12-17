from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.generated.sreen_sobre_programa as uiSobre
from globais import *



class SobreSistema(uiSobre.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.iniciar_tela()
        self.preencher_informacoes()

    def iniciar_tela(self):
        self.ui = uiSobre.Ui_Form()
        self.ui.setupUi(self)

    def preencher_informacoes(self):
        self.ui.lbDataRevisao.setText(RELEASED)
        self.ui.lbDesenvolvedor.setText(BY)
        self.ui.lbSite.setText(WEBSITE)
        self.ui.lbSoftware.setText(APP)
        self.ui.lbVersao.setText(VERSION)
        self.ui.lbPastaBase.setText(PASTA_BASE)
        self.ui.lbDataBase.setText(SQL_FILE)