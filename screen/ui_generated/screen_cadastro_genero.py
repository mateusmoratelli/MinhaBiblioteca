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
        self.lstGeneros.setGeometry(QtCore.QRect(30, 90, 251, 371))
        self.lstGeneros.setObjectName("lstGeneros")
        item = QtWidgets.QListWidgetItem()
        self.lstGeneros.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstGeneros.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstGeneros.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstGeneros.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstGeneros.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstGeneros.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstGeneros.addItem(item)
        self.btSalvarGenero = QtWidgets.QPushButton(Form)
        self.btSalvarGenero.setGeometry(QtCore.QRect(300, 150, 121, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/save_16dp_48752C.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSalvarGenero.setIcon(icon)
        self.btSalvarGenero.setIconSize(QtCore.QSize(24, 24))
        self.btSalvarGenero.setObjectName("btSalvarGenero")
        self.txtGenero = QtWidgets.QLineEdit(Form)
        self.txtGenero.setGeometry(QtCore.QRect(300, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtGenero.setFont(font)
        self.txtGenero.setObjectName("txtGenero")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 90, 121, 16))
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
        self.btExcluirGenero.setGeometry(QtCore.QRect(500, 150, 121, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("screen/ui_designer\\../../resources/icons/delete_forever_16dp_BB271A.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btExcluirGenero.setIcon(icon1)
        self.btExcluirGenero.setIconSize(QtCore.QSize(24, 24))
        self.btExcluirGenero.setObjectName("btExcluirGenero")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro de Gêneros de Livros"))
        self.label.setText(_translate("Form", "CADASTRO DE GÊNERO DE LIVROS"))
        __sortingEnabled = self.lstGeneros.isSortingEnabled()
        self.lstGeneros.setSortingEnabled(False)
        item = self.lstGeneros.item(0)
        item.setText(_translate("Form", "New Item"))
        item = self.lstGeneros.item(1)
        item.setText(_translate("Form", "New Item"))
        item = self.lstGeneros.item(2)
        item.setText(_translate("Form", "New Item"))
        item = self.lstGeneros.item(3)
        item.setText(_translate("Form", "New Item"))
        item = self.lstGeneros.item(4)
        item.setText(_translate("Form", "New Item"))
        item = self.lstGeneros.item(5)
        item.setText(_translate("Form", "New Item"))
        item = self.lstGeneros.item(6)
        item.setText(_translate("Form", "New Item"))
        self.lstGeneros.setSortingEnabled(__sortingEnabled)
        self.btSalvarGenero.setText(_translate("Form", "Salvar Gênero"))
        self.label_2.setText(_translate("Form", "Gênero"))
        self.label_3.setText(_translate("Form", "Gêneros Cadastrados"))
        self.btExcluirGenero.setText(_translate("Form", "Excluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
