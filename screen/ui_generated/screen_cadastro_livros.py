# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen/ui_designer/screen_cadastro_livros.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(794, 612)
        Form.setMaximumSize(QtCore.QSize(999999, 999999))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 761, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btSalvar = QtWidgets.QPushButton(Form)
        self.btSalvar.setGeometry(QtCore.QRect(660, 550, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btSalvar.setFont(font)
        self.btSalvar.setObjectName("btSalvar")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 491, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtLivro = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtLivro.setFont(font)
        self.txtLivro.setObjectName("txtLivro")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtLivro)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtAutor = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAutor.setFont(font)
        self.txtAutor.setObjectName("txtAutor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtAutor)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtEditora = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEditora.setFont(font)
        self.txtEditora.setObjectName("txtEditora")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtEditora)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cbGenero = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbGenero.setFont(font)
        self.cbGenero.setObjectName("cbGenero")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbGenero)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtIsbn = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtIsbn.setFont(font)
        self.txtIsbn.setObjectName("txtIsbn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtIsbn)
        self.lbCapa = QtWidgets.QLabel(Form)
        self.lbCapa.setGeometry(QtCore.QRect(10, 230, 241, 311))
        self.lbCapa.setText("")
        self.lbCapa.setPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/img/figura2.png"))
        self.lbCapa.setObjectName("lbCapa")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(510, 60, 271, 161))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txtPaginas = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPaginas.setFont(font)
        self.txtPaginas.setObjectName("txtPaginas")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtPaginas)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtAno = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAno.setFont(font)
        self.txtAno.setObjectName("txtAno")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtAno)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.sliderClassificacao = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.sliderClassificacao.setMaximum(5)
        self.sliderClassificacao.setProperty("value", 3)
        self.sliderClassificacao.setOrientation(QtCore.Qt.Horizontal)
        self.sliderClassificacao.setObjectName("sliderClassificacao")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sliderClassificacao)
        self.txtSinopse = QtWidgets.QTextEdit(Form)
        self.txtSinopse.setGeometry(QtCore.QRect(250, 230, 531, 311))
        self.txtSinopse.setObjectName("txtSinopse")
        self.btAlterarCapa = QtWidgets.QPushButton(Form)
        self.btAlterarCapa.setGeometry(QtCore.QRect(10, 550, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAlterarCapa.setFont(font)
        self.btAlterarCapa.setObjectName("btAlterarCapa")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "CADASTRO DE LIVROS"))
        self.btSalvar.setText(_translate("Form", "Salvar Livro"))
        self.label_2.setText(_translate("Form", "Livro"))
        self.label_3.setText(_translate("Form", "Autor"))
        self.label_4.setText(_translate("Form", "Editora"))
        self.label_5.setText(_translate("Form", "Genero"))
        self.label_6.setText(_translate("Form", "ISBN"))
        self.label_8.setText(_translate("Form", "Páginas"))
        self.label_9.setText(_translate("Form", "Ano Publicação"))
        self.label_10.setText(_translate("Form", "Classificação"))
        self.btAlterarCapa.setText(_translate("Form", "Alterar capa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
