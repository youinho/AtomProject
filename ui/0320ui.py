# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '0319ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 820, 401))
        self.groupBox.setObjectName("groupBox")
        self.gdsdfsd = QtWidgets.QTabWidget(self.groupBox)
        self.gdsdfsd.setGeometry(QtCore.QRect(20, 30, 781, 351))
        self.gdsdfsd.setMinimumSize(QtCore.QSize(651, 351))
        self.gdsdfsd.setSizeIncrement(QtCore.QSize(302, 0))
        self.gdsdfsd.setTabPosition(QtWidgets.QTabWidget.North)
        self.gdsdfsd.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.gdsdfsd.setIconSize(QtCore.QSize(100, 16))
        self.gdsdfsd.setObjectName("gdsdfsd")
        self.widget = QtWidgets.QWidget()
        self.widget.setEnabled(True)
        self.widget.setBaseSize(QtCore.QSize(3, 0))
        self.widget.setObjectName("widget")
        self.gdsdfsd.addTab(self.widget, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gdsdfsd.addTab(self.tabWidgetPage2, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(19, 419, 801, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setGeometry(QtCore.QRect(50, 50, 771, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 770, 121, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.gdsdfsd.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.gdsdfsd.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">dsffdsff</span></p></body></html>"))
        self.gdsdfsd.setTabText(self.gdsdfsd.indexOf(self.widget), _translate("MainWindow", "개요"))
        self.gdsdfsd.setTabText(self.gdsdfsd.indexOf(self.tabWidgetPage2), _translate("MainWindow", "예방정책"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "지도로보기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
