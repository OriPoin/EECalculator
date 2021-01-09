# Test Window
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout,QLineEdit,QPushButton
from PySide2.QtCore import Qt, QSize, QMargins
import math

import schemdraw
import schemdraw.elements as elm

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
sys.path.append('../EECalculator')
from EECalculator.HomePage import config

# Define Your Calculator


class Opreator(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout(self)
        self.setMinimumSize(600,300)
        self.LableR=QLabel("电阻（Ω）")
        self.layout.addWidget(self.LableR,0,0)
        self.LableR.setAlignment(Qt.AlignCenter)
        self.LableC=QLabel("电容（uF）")
        self.layout.addWidget(self.LableC,0,1)
        self.LableC.setAlignment(Qt.AlignCenter)
        self.LableF=QLabel("截至频率（Hz）")
        self.layout.addWidget(self.LableF,0,2)
        self.LableF.setAlignment(Qt.AlignCenter)
        self.EditR=QLineEdit()
        self.layout.addWidget(self.EditR,1,0)
        self.EditC=QLineEdit()
        self.layout.addWidget(self.EditC,1,1)
        self.ShowF=QLineEdit()
        self.layout.addWidget(self.ShowF,1,2)
        self.opbtn=QPushButton("计算")
        self.layout.addWidget(self.opbtn,2,1)
        self.opbtn.clicked.connect(self.op)

    def op(self):
        r=float(self.EditR.text())
        c=float(self.EditC.text())
        f=1000000/(2*math.pi*r*c)
        self.ShowF.setText(str(f))



class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout(self)
        # # self.imgwidget = QLabel(self)
        # Plot RC filter
        rc = schemdraw.Drawing()
        rc.add(elm.Resistor(d='right', label='R', lftlabel='In', rgtlabel='Out'))
        rc.add(elm.Capacitor(d='down', label='C'))
        rc.add(elm.Ground(d='right'))
        # rc.draw(show=False)
        rccanvas = FigureCanvas(rc.draw(show=False).getfig())
        self.layout.addWidget(rccanvas,0,0,2,1)
        self.layout.setMargin(0)
        self.layout.setSpacing(0)
        self.InputWidget=Opreator()
        self.layout.addWidget(self.InputWidget)

# Test Window

class Calculator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.MainWidget = MainWidget()
        self.SetupWindow()

    def SetupWindow(self):
        # Set Window Size
        self.resize(600, 600)
        self.setMinimumSize(QSize(600, 600))
        # Set Window Titile
        self.setWindowTitle(type(self.MainWidget).__name__)
        self.setCentralWidget(self.MainWidget)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
