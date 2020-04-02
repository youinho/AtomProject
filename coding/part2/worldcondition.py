from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib import style
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from world import *
import world_condition

class class_condition(QWidget,world_condition.Ui_Form):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.w_definite = world_condition_definite
        self.w_death = world_condition_death
        self.death_index.setText(world_condition_death)
        self.definite_index.setText(world_condition_definite)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = class_condition()
    window.show()
    app.exec_()
