import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.setLayout(self.layout)
        self.setGeometry(200,200,800,600)

    def initUI(self):
        # information of groups

        group_names = ['Group_A', 'Group_B', 'Group_C']

        group_sizes = [95, 54, 25]

        group_colors = ['yellowgreen', 'lightskyblue', 'lightcoral']

        group_explodes = (0.1, 0, 0) # explode 1st slice

        plt.pie(group_sizes,

                explode=group_explodes,

                labels=group_names,

                colors=group_colors,

                autopct='%1.2f%%', # second decimal place

                shadow=True,

                startangle=90,

                textprops={'fontsize': 14}) # text font size

        plt.axis('equal') #  equal length of X and Y axis

        plt.title('Pie Chart of Market Share', fontsize=20)
        self.fig = plt.Figure()
    #figure 그래프 창 설정 -> canvas 그래프 표시 창
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
    #vertical BoxLayout () - 수평
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.layout = layout
        self.layout.draw()
        self.layout.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
