from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.ui_generated.sreen_sobre_programa as uiSobre
from contantes import *



class SobreSistema(uiSobre.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarTela()
        self.preencheInformacoes()

    def iniciarTela(self):
        self.ui = uiSobre.Ui_Form()
        self.ui.setupUi(self)

    def preencheInformacoes(self):
        self.ui.lbDataRevisao.setText(RELEASED)
        self.ui.lbDesenvolvedor.setText(BY)
        self.ui.lbSite.setText(WEBSITE)
        self.ui.lbSoftware.setText(APP)
        self.ui.lbVersao.setText(VERSION)
    
 

        