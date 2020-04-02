import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import ui.world_page_ui as ui
from coding.part2.world_bar import *
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
import urllib.request as req
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from statistics import *
from matplotlib import font_manager, rc
from matplotlib import style
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from coding.part2.world_list import *
from coding.part2.world import *


class page_world(QWidget,ui.Ui_Form):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.w = world_chart(self)
        self.w.setGeometry(QtCore.QRect(0, 100, 550, 600))
        self.searchButton.clicked.connect(self.click)
        self.definite_index.setText("전세계 확진자 : "+world_condition_definite)
        self.death_index.setText("전세계 사망자 : "+world_condition_death)
        self.definite_index.setGeometry(QtCore.QRect(100,50,200,50))
        self.death_index.setGeometry(QtCore.QRect(350,50,200,50))
        self.setTableWidgetData(self.w.get_many())
        self.radioButton_little.clicked.connect(self.radio1)
        self.radioButton_many.clicked.connect(self.radio2)

    def radio1(self):
        self.setTableWidgetData(little)

    def radio2(self) :
        self.setTableWidgetData(many)

    def click(self) :
        item=self.nationInput.text()
        if item in nation:
            ix=nation.index(item)
            value=nation_value[ix]
            di =dict({item:value[:-1]})
            self.setTableWidgetData(di)
        else:
            self.nationInput.clear()


    def setTableWidgetData(self,dict_data):
        self.tableWidget.setRowCount(len(dict_data))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["나라","확진자 수"])
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.resizeRowsToContents()
        i=0
        for index,(key,elem) in enumerate(dict_data.items()) :
            j=0
            self.tableWidget.setItem(i,j,QTableWidgetItem(key))
            j+=1
            self.tableWidget.setItem(i,j,QTableWidgetItem(str(elem)+"명"))
            i+=1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = page_world()
    window.show()
    app.exec_()
