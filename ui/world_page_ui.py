# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 700)
        self.definite_index = QtWidgets.QLabel(Form)
        self.definite_index.setGeometry(QtCore.QRect(100, 20, 231, 71))
        self.definite_index.setObjectName("label")
        self.death_index = QtWidgets.QLabel(Form)
        self.death_index.setGeometry(QtCore.QRect(200, 20, 231, 71))
        self.death_index.setObjectName("definite")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(555, 200, 181, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.nationInput = QtWidgets.QLineEdit(Form)
        self.nationInput.setGeometry(QtCore.QRect(570, 140, 151, 20))
        self.nationInput.setObjectName("lineEdit")
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(610, 170, 75, 23))
        self.searchButton.setObjectName("searchButton")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(560, 10, 181, 111))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_little = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_little.setGeometry(QtCore.QRect(20, 85, 141, 16))
        self.radioButton_little.setObjectName("radioButton_many")
        self.radioButton_many = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_many.setGeometry(QtCore.QRect(20, 50, 131, 16))
        self.radioButton_many.setObjectName("radioButton_many")
        self.definite = QtWidgets.QLabel(Form)
        self.definite.setGeometry(QtCore.QRect(290, 20, 221, 31))
        self.definite.setObjectName("definite")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchButton.setText(_translate("Form", "검색"))
        self.definite_index.setText(_translate("Form", "세계 확진자 수 : "))
        self.death_index.setText(_translate("Form", "세계 사망자 수 :"))
        self.searchButton.setText(_translate("MainWindow", "검색"))
        self.groupBox.setTitle(_translate("MainWindow", "선택"))
        self.radioButton_little.setText(_translate("MainWindow", "확진자 낮은순"))
        self.radioButton_many.setText(_translate("MainWindow", "확진자 높은순"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
