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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 740, 47, 13))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(750, 70, 521, 611))
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
        self.lbTituloLivro = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbTituloLivro.setFont(font)
        self.lbTituloLivro.setObjectName("lbTituloLivro")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbTituloLivro)
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
        self.lbAnoPublicacao = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbAnoPublicacao.setFont(font)
        self.lbAnoPublicacao.setObjectName("lbAnoPublicacao")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lbAnoPublicacao)
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
        self.txtSinopse = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txtSinopse.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSinopse.setFont(font)
        self.txtSinopse.setObjectName("txtSinopse")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.txtSinopse)
        self.btLerResumo = QtWidgets.QPushButton(self.centralwidget)
        self.btLerResumo.setGeometry(QtCore.QRect(600, 630, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btLerResumo.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/local_library_16dp_5F6368.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btLerResumo.setIcon(icon)
        self.btLerResumo.setIconSize(QtCore.QSize(24, 24))
        self.btLerResumo.setObjectName("btLerResumo")
        self.btAbrirPDF = QtWidgets.QPushButton(self.centralwidget)
        self.btAbrirPDF.setEnabled(False)
        self.btAbrirPDF.setGeometry(QtCore.QRect(600, 570, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAbrirPDF.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/picture_as_pdf_16dp_5F6368.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btAbrirPDF.setIcon(icon1)
        self.btAbrirPDF.setIconSize(QtCore.QSize(24, 24))
        self.btAbrirPDF.setObjectName("btAbrirPDF")
        self.btBuscarLivros = QtWidgets.QPushButton(self.centralwidget)
        self.btBuscarLivros.setGeometry(QtCore.QRect(360, 3, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btBuscarLivros.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/search_24dp_5F6368.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btBuscarLivros.setIcon(icon2)
        self.btBuscarLivros.setIconSize(QtCore.QSize(24, 24))
        self.btBuscarLivros.setObjectName("btBuscarLivros")
        self.btNovoLivro = QtWidgets.QPushButton(self.centralwidget)
        self.btNovoLivro.setGeometry(QtCore.QRect(470, 570, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btNovoLivro.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/library_books_16dp_5F6368.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btNovoLivro.setIcon(icon3)
        self.btNovoLivro.setIconSize(QtCore.QSize(24, 24))
        self.btNovoLivro.setObjectName("btNovoLivro")
        self.lbCapa = QtWidgets.QLabel(self.centralwidget)
        self.lbCapa.setGeometry(QtCore.QRect(450, 70, 291, 371))
        self.lbCapa.setAutoFillBackground(False)
        self.lbCapa.setText("")
        self.lbCapa.setPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/img/capa_programa_principal.png"))
        self.lbCapa.setScaledContents(True)
        self.lbCapa.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbCapa.setWordWrap(False)
        self.lbCapa.setObjectName("lbCapa")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 4, 281, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btEditarLivro = QtWidgets.QPushButton(self.centralwidget)
        self.btEditarLivro.setGeometry(QtCore.QRect(470, 630, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btEditarLivro.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/border_color_16dp_5F6368.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btEditarLivro.setIcon(icon4)
        self.btEditarLivro.setIconSize(QtCore.QSize(24, 24))
        self.btEditarLivro.setObjectName("btEditarLivro")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(470, 500, 62, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.cbUsuarios = QtWidgets.QComboBox(self.centralwidget)
        self.cbUsuarios.setGeometry(QtCore.QRect(470, 530, 249, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbUsuarios.setFont(font)
        self.cbUsuarios.setObjectName("cbUsuarios")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lstLivros = QtWidgets.QListWidget(self.centralwidget)
        self.lstLivros.setGeometry(QtCore.QRect(20, 70, 421, 611))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lstLivros.setFont(font)
        self.lstLivros.setObjectName("lstLivros")
        item = QtWidgets.QListWidgetItem()
        self.lstLivros.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstLivros.addItem(item)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 450, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lbID = QtWidgets.QLabel(self.centralwidget)
        self.lbID.setGeometry(QtCore.QRect(510, 450, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbID.setFont(font)
        self.lbID.setObjectName("lbID")
        self.btAtualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btAtualizar.setGeometry(QtCore.QRect(450, 0, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAtualizar.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/refresh_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btAtualizar.setIcon(icon5)
        self.btAtualizar.setIconSize(QtCore.QSize(24, 24))
        self.btAtualizar.setObjectName("btAtualizar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1313, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastrar = QtWidgets.QMenu(self.menubar)
        self.menuCadastrar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuCadastrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuCadastrar.setObjectName("menuCadastrar")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuNovoLivro = QtWidgets.QAction(MainWindow)
        self.menuNovoLivro.setObjectName("menuNovoLivro")
        self.menuCadatrarGenero = QtWidgets.QAction(MainWindow)
        self.menuCadatrarGenero.setObjectName("menuCadatrarGenero")
        self.menuCadastrarUsuario = QtWidgets.QAction(MainWindow)
        self.menuCadastrarUsuario.setObjectName("menuCadastrarUsuario")
        self.actionResumo = QtWidgets.QAction(MainWindow)
        self.actionResumo.setObjectName("actionResumo")
        self.menuEfetuarTestes = QtWidgets.QAction(MainWindow)
        self.menuEfetuarTestes.setObjectName("menuEfetuarTestes")
        self.menuSobrePrograma = QtWidgets.QAction(MainWindow)
        self.menuSobrePrograma.setObjectName("menuSobrePrograma")
        self.menuEfetuarTeste = QtWidgets.QAction(MainWindow)
        self.menuEfetuarTeste.setObjectName("menuEfetuarTeste")
        self.menuCadastrar.addAction(self.menuNovoLivro)
        self.menuCadastrar.addAction(self.menuCadatrarGenero)
        self.menuCadastrar.addSeparator()
        self.menuCadastrar.addAction(self.menuCadastrarUsuario)
        self.menuAjuda.addAction(self.menuSobrePrograma)
        self.menuAjuda.addSeparator()
        self.menuAjuda.addAction(self.menuEfetuarTeste)
        self.menubar.addAction(self.menuCadastrar.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minha Biblioteca"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Título"))
        self.lbTituloLivro.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "Autor"))
        self.lbAutor.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Editora"))
        self.lbEditora.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Gênero"))
        self.lbGenero.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "ISBN"))
        self.lbIsbn.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "Ano publicação"))
        self.lbAnoPublicacao.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "PDF"))
        self.lbPDF.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "Páginas"))
        self.lbPaginas.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "Páginas Lidas"))
        self.lbPaginasLidas.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "Classfiicação"))
        self.lbClassificacao.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "Sinopse"))
        self.btLerResumo.setText(_translate("MainWindow", "Ler Resumo"))
        self.btAbrirPDF.setText(_translate("MainWindow", "Abrir PDF"))
        self.btBuscarLivros.setText(_translate("MainWindow", "Buscar"))
        self.btNovoLivro.setText(_translate("MainWindow", "Novo Livro"))
        self.label_3.setText(_translate("MainWindow", "Buscar"))
        self.btEditarLivro.setText(_translate("MainWindow", "Editar Livro"))
        self.label_21.setText(_translate("MainWindow", "Usuário"))
        self.label_5.setText(_translate("MainWindow", "Lista de Livros"))
        __sortingEnabled = self.lstLivros.isSortingEnabled()
        self.lstLivros.setSortingEnabled(False)
        item = self.lstLivros.item(0)
        item.setText(_translate("MainWindow", "item1"))
        item = self.lstLivros.item(1)
        item.setText(_translate("MainWindow", "item2"))
        self.lstLivros.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "ID"))
        self.lbID.setText(_translate("MainWindow", "0000"))
        self.btAtualizar.setText(_translate("MainWindow", "Atualizar"))
        self.menuCadastrar.setTitle(_translate("MainWindow", "Cadastrar"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.menuNovoLivro.setText(_translate("MainWindow", "Novo Livro"))
        self.menuCadatrarGenero.setText(_translate("MainWindow", "Cadastrar Gênero de livro"))
        self.menuCadastrarUsuario.setText(_translate("MainWindow", "Usuários"))
        self.actionResumo.setText(_translate("MainWindow", "Resumo"))
        self.menuEfetuarTestes.setText(_translate("MainWindow", " Efetuar Testes DB"))
        self.menuSobrePrograma.setText(_translate("MainWindow", "Sobre o programa"))
        self.menuEfetuarTeste.setText(_translate("MainWindow", "Efetuar Testes DB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
