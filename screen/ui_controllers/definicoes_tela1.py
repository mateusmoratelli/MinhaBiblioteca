from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import screen.ui_generated.screen01_machine_input_datas as ui01  # Importe a primeira tela
import screen.ui_controllers.definicoes_tela2 as load_tela2
import test.user_crud_test as _testCrud

 


class screen01():
    """
        ESTA CLASSE TRABALHA COM OS DADO DA TELA 1 
    """
    def __init__(self):
        """Inicializador da classe"""

        # aqui cada função que vai iniciar para configurar a tela 
        self.iniciarAplicacao()
        self.defineFuncoesDosBotoes()
        self.parametrosIniciaisTela01()
        self.popularComboBoxs()
        self.carregarImagem()
        sys.exit(self.app.exec_())


    # --------------------------------------------------------------------------------------------- #
    def iniciarAplicacao(self):
        """Inicia a aplicação"""
        self.app = ui01.QtWidgets.QApplication(sys.argv)    # define o app
        self.Screen01 = ui01.QtWidgets.QMainWindow()        # define a screen main
        self.ui = ui01.Ui_Screen01()                        # nomeia como self.ui a tela Screen01
        self.ui.setupUi(self.Screen01)                      # configura a tela inicial 
        self.Screen01.show()                                # exibe a tela.


    # --------------------------------------------------------------------------------------------- #
    def defineFuncoesDosBotoes(self):
         """Definir cada botão a sua ação, incluindo menus"""
         self.ui.menu_teste.triggered.connect(self.botaoMenu1ApenasImprime)     # configura a ação do menu1
         self.ui.menu_tela2.triggered.connect(self.botaoAbreTela2)              # configura a ação do menu2

         self.ui.bt_Update01.clicked.connect(self.botaoUpdate)                  # configura a ação do botão update
         self.ui.bt_MachineInputDatas.clicked.connect(self.botaoMachineData)    # configura a ação do botão 


    # --------------------------------------------------------------------------------------------- #
    def parametrosIniciaisTela01(self):
        """Paramêtros para inicializar a tela, ou seja tudo o que tiver valor inicial"""
        self.ui.label17.setText("MY LABEL 17")          
        self.ui.label18.setText("MY LABEL 18")
        

    # --------------------------------------------------------------------------------------------- #
    def popularComboBoxs(self): 
        # Combobox - Type Machine
        self.ui.cbTypeMachine.clear() 
        self.ui.cbTypeMachine.addItems(["ABC", "DEF", "GHI", "JKL"])

        # Combobox - Frequencia 
        self.ui.cbFrequency.clear() 
        self.ui.cbFrequency.addItems(["", "50", "60"])

        # Combobox - cbPole
        self.ui.cbPole.clear()
        for i in range(2, 41, 2):
            self.ui.cbPole.addItem(str(i))


    # --------------------------------------------------------------------------------------------- #
    def botaoMenu1ApenasImprime(self):
        print("menu de teste clicado.") # apenas teste
        _testCrud.mainTestCrud()


    # --------------------------------------------------------------------------------------------- #  
    def carregarImagem(self):
        if self.ui.cbFrequency.currentText() == "60":        # pega o valor do combo da frequência e verifica se é igual a 60
            pixmap = QtGui.QPixmap("resources/img/figura1.png")             # Substitua pelo caminho real da imagem
        elif self.ui.cbFrequency.currentText() == "50":    
            pixmap = QtGui.QPixmap("resources/img/figura2.png")             # Substitua pelo caminho real da imagem
        else:
            pixmap = QtGui.QPixmap("resources/img/figura_inicial.png")      # Substitua pelo caminho real da imagem
        
        self.ui.labelPicture01.setPixmap(pixmap)                            # Seta um pixmap
        self.ui.labelPicture01.setScaledContents(True)                      # Ajusta a imagem para ocupar todo o espaço do QLabel 


    # --------------------------------------------------------------------------------------------- #
    def botaoAbreTela2(self):
       print("botão tela 2 clicado.")
       self.tela2 = load_tela2.screen02()
       self.tela2.show()


    # --------------------------------------------------------------------------------------------- #
    def botaoUpdate(self):
        print("botão update clicado. - Altere a frequência para alterar a imagem.")  
        print(self.ui.cbFrequency.currentText())
        self.carregarImagem()

    # --------------------------------------------------------------------------------------------- #
    def botaoMachineData(self):
        print("botão machine data clicado.")
