# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen/ui_designer/sreen_sobre_programa.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 226)
        self.lbSoftware = QtWidgets.QLabel(Dialog)
        self.lbSoftware.setGeometry(QtCore.QRect(10, 10, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbSoftware.setFont(font)
        self.lbSoftware.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSoftware.setObjectName("lbSoftware")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 79, 451, 121))
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
        self.lbVersao = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbVersao.setFont(font)
        self.lbVersao.setObjectName("lbVersao")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbVersao)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lbDataRevisao = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbDataRevisao.setFont(font)
        self.lbDataRevisao.setObjectName("lbDataRevisao")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbDataRevisao)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lbDesenvolvedor = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbDesenvolvedor.setFont(font)
        self.lbDesenvolvedor.setObjectName("lbDesenvolvedor")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbDesenvolvedor)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lbSite = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbSite.setFont(font)
        self.lbSite.setObjectName("lbSite")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lbSite)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sobre o Programa"))
        self.lbSoftware.setText(_translate("Dialog", "PROGRAMA XXXX"))
        self.label_2.setText(_translate("Dialog", "Versão:"))
        self.lbVersao.setText(_translate("Dialog", "XXX"))
        self.label_3.setText(_translate("Dialog", "Data:"))
        self.lbDataRevisao.setText(_translate("Dialog", "XXX"))
        self.label_4.setText(_translate("Dialog", "Desenvolvedor:  "))
        self.lbDesenvolvedor.setText(_translate("Dialog", "XXX"))
        self.label_5.setText(_translate("Dialog", "Site:"))
        self.lbSite.setText(_translate("Dialog", "XXX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())