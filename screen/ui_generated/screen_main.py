# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen/ui_designer/screen_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbLivros = QtWidgets.QTableWidget(self.centralwidget)
        self.tbLivros.setGeometry(QtCore.QRect(10, 20, 431, 611))
        self.tbLivros.setObjectName("tbLivros")
        self.tbLivros.setColumnCount(1)
        self.tbLivros.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbLivros.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbLivros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbLivros.setItem(0, 0, item)
        self.tbLivros.horizontalHeader().setDefaultSectionSize(450)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 740, 47, 13))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(750, 20, 551, 611))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lbAutor = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbAutor.setFont(font)
        self.lbAutor.setObjectName("lbAutor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbAutor)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lbEditora = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbEditora.setFont(font)
        self.lbEditora.setObjectName("lbEditora")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbEditora)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lbGenero = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbGenero.setFont(font)
        self.lbGenero.setObjectName("lbGenero")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lbGenero)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lbIsbn = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbIsbn.setFont(font)
        self.lbIsbn.setObjectName("lbIsbn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lbIsbn)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lbPDF = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbPDF.setFont(font)
        self.lbPDF.setObjectName("lbPDF")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lbPDF)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lbPaginas = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbPaginas.setFont(font)
        self.lbPaginas.setObjectName("lbPaginas")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lbPaginas)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lbClassificacao = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbClassificacao.setFont(font)
        self.lbClassificacao.setObjectName("lbClassificacao")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lbClassificacao)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lbAnoPublicacao = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbAnoPublicacao.setFont(font)
        self.lbAnoPublicacao.setObjectName("lbAnoPublicacao")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lbAnoPublicacao)
        self.lbTituloLivro = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbTituloLivro.setFont(font)
        self.lbTituloLivro.setObjectName("lbTituloLivro")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbTituloLivro)
        self.txtSinopse = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txtSinopse.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSinopse.setFont(font)
        self.txtSinopse.setObjectName("txtSinopse")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.txtSinopse)
        self.cbUsuarios = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbUsuarios.setFont(font)
        self.cbUsuarios.setObjectName("cbUsuarios")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.cbUsuarios)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lbPaginasLidas = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbPaginasLidas.setFont(font)
        self.lbPaginasLidas.setObjectName("lbPaginasLidas")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lbPaginasLidas)
        self.btLerResumo = QtWidgets.QPushButton(self.centralwidget)
        self.btLerResumo.setGeometry(QtCore.QRect(520, 400, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btLerResumo.setFont(font)
        self.btLerResumo.setObjectName("btLerResumo")
        self.btAbrirPDF = QtWidgets.QPushButton(self.centralwidget)
        self.btAbrirPDF.setGeometry(QtCore.QRect(520, 520, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAbrirPDF.setFont(font)
        self.btAbrirPDF.setObjectName("btAbrirPDF")
        self.btEditarLivro = QtWidgets.QPushButton(self.centralwidget)
        self.btEditarLivro.setGeometry(QtCore.QRect(520, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btEditarLivro.setFont(font)
        self.btEditarLivro.setObjectName("btEditarLivro")
        self.btNovoLivro = QtWidgets.QPushButton(self.centralwidget)
        self.btNovoLivro.setGeometry(QtCore.QRect(520, 580, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btNovoLivro.setFont(font)
        self.btNovoLivro.setObjectName("btNovoLivro")
        self.lbCapa = QtWidgets.QLabel(self.centralwidget)
        self.lbCapa.setGeometry(QtCore.QRect(450, 20, 291, 371))
        self.lbCapa.setAutoFillBackground(False)
        self.lbCapa.setText("")
        self.lbCapa.setPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/img/figura1.png"))
        self.lbCapa.setScaledContents(True)
        self.lbCapa.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbCapa.setWordWrap(False)
        self.lbCapa.setObjectName("lbCapa")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1313, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastrar = QtWidgets.QMenu(self.menubar)
        self.menuCadastrar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuCadastrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuCadastrar.setObjectName("menuCadastrar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuNovoLivro = QtWidgets.QAction(MainWindow)
        self.menuNovoLivro.setObjectName("menuNovoLivro")
        self.menuCadatrarCategoria = QtWidgets.QAction(MainWindow)
        self.menuCadatrarCategoria.setObjectName("menuCadatrarCategoria")
        self.menuCadastrarUsuario = QtWidgets.QAction(MainWindow)
        self.menuCadastrarUsuario.setObjectName("menuCadastrarUsuario")
        self.actionResumo = QtWidgets.QAction(MainWindow)
        self.actionResumo.setObjectName("actionResumo")
        self.menuCadastrar.addAction(self.menuNovoLivro)
        self.menuCadastrar.addAction(self.menuCadatrarCategoria)
        self.menuCadastrar.addSeparator()
        self.menuCadastrar.addAction(self.menuCadastrarUsuario)
        self.menubar.addAction(self.menuCadastrar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tbLivros.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "01"))
        item = self.tbLivros.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Livro"))
        __sortingEnabled = self.tbLivros.isSortingEnabled()
        self.tbLivros.setSortingEnabled(False)
        self.tbLivros.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Título"))
        self.label_4.setText(_translate("MainWindow", "Autor"))
        self.lbAutor.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Editora"))
        self.lbEditora.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Gênero"))
        self.lbGenero.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "ISBN"))
        self.lbIsbn.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "Ano publicação"))
        self.label_16.setText(_translate("MainWindow", "PDF"))
        self.lbPDF.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "Páginas"))
        self.lbPaginas.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "Classfiicação"))
        self.lbClassificacao.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "Sinopse"))
        self.lbAnoPublicacao.setText(_translate("MainWindow", "TextLabel"))
        self.lbTituloLivro.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "Usuário"))
        self.label_13.setText(_translate("MainWindow", "Páginas Lidas"))
        self.lbPaginasLidas.setText(_translate("MainWindow", "TextLabel"))
        self.btLerResumo.setText(_translate("MainWindow", "Ler Resumo"))
        self.btAbrirPDF.setText(_translate("MainWindow", "Abrir PDF"))
        self.btEditarLivro.setText(_translate("MainWindow", "Editar Livro"))
        self.btNovoLivro.setText(_translate("MainWindow", "Novo Livro"))
        self.menuCadastrar.setTitle(_translate("MainWindow", "Cadastrar"))
        self.menuNovoLivro.setText(_translate("MainWindow", "Novo Livro"))
        self.menuCadatrarCategoria.setText(_translate("MainWindow", "Categorias"))
        self.menuCadastrarUsuario.setText(_translate("MainWindow", "Usuários"))
        self.actionResumo.setText(_translate("MainWindow", "Resumo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
