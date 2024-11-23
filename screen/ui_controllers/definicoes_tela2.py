from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import screen.ui_generated.screen02_tela_teste as _ui02  # Importe a segunda tela
import core.calculo1 as _calc1

 
class screen02(_ui02.QtWidgets.QWidget):  # Herda de QWidget ou QMainWindow conforme necessário
    def __init__(self):
        super().__init__()
        self.iniciarAplicacao()
        self.parametrosIniciaisTela02()
        self.acoesDosBotoes()

    # --------------------------------------------------------------------------------------------- #
    def iniciarAplicacao(self):
        self.ui = _ui02.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Segunda Tela")


    # --------------------------------------------------------------------------------------------- #
    def parametrosIniciaisTela02(self):
        print("Meus parâmetros iniciais da Tela 02")


    # --------------------------------------------------------------------------------------------- #
    def acoesDosBotoes(self):
        """Definir toda as ações de cada botão."""
        self.ui.pushButton.clicked.connect(self.botaoOkClicado)
    

    # --------------------------------------------------------------------------------------------- #
    def botaoOkClicado(self): 
        """
          Esta função executa as ações dos botões, 
          NÃO incluir esta função no __init__
        """
        valor1 = int(self.ui.txt_valor1.text())     # pega o valor 1
        valor2 = int(self.ui.txt_valor2.text())     # paga o valor 2
        valor3 = int(self.ui.txt_valor3.text())     # pega o valor 3
        # self.resultado = valor1 + valor2 + valor3 
        self.resultado = _calc1.somavalores(valor1, valor2, valor3)

        #  imprime valores  no console. 
        print("O botão OK foi clicado")
        print(f"Valor 1: {valor1}")
        print(f"Valor 2: {valor2}")
        print(f"Valor 3: {valor3}")
        print(f"O resultado é {self.resultado}")

        self.ui.lb_resposta.setText(f"O resultado é: {self.resultado}")

    
 







 

