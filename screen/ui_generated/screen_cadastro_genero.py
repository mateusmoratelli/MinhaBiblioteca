# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen/ui_designer/screen_cadastro_genero.ui'
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
        Form.resize(640, 480)
        Form.setMaximumSize(QtCore.QSize(640, 480))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lstGeneros = QtWidgets.QListWidget(Form)
        self.lstGeneros.setGeometry(QtCore.QRect(30, 90, 251, 321))
        self.lstGeneros.setObjectName("lstGeneros")
        self.btSalvarGenero = QtWidgets.QPushButton(Form)
        self.btSalvarGenero.setGeometry(QtCore.QRect(360, 130, 121, 51))
        self.btSalvarGenero.setObjectName("btSalvarGenero")
        self.txtGenero = QtWidgets.QLineEdit(Form)
        self.txtGenero.setGeometry(QtCore.QRect(360, 90, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtGenero.setFont(font)
        self.txtGenero.setObjectName("txtGenero")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btExcluirGenero = QtWidgets.QPushButton(Form)
        self.btExcluirGenero.setGeometry(QtCore.QRect(160, 420, 121, 51))
        self.btExcluirGenero.setObjectName("btExcluirGenero")
        self.btEditarGenero = QtWidgets.QPushButton(Form)
        self.btEditarGenero.setGeometry(QtCore.QRect(30, 420, 121, 51))
        self.btEditarGenero.setObjectName("btEditarGenero")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro de Gêneros de Livros"))
        self.label.setText(_translate("Form", "CADASTRO DE GÊNERO DE LIVROS"))
        self.btSalvarGenero.setText(_translate("Form", "Salvar Gênero"))
        self.label_2.setText(_translate("Form", "Novo Gênero"))
        self.label_3.setText(_translate("Form", "Gêneros Cadastrados"))
        self.btExcluirGenero.setText(_translate("Form", "Excluir"))
        self.btEditarGenero.setText(_translate("Form", "Editar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())