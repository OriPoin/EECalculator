#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import schemdraw.elements as elm
import schemdraw
import sys
sys.path.append('../EECalculator')
from EECalculator.HomePage import config
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel,QLineEdit,QPushButton
from PySide2.QtCore import Qt, QSize, QMargins



matplotlib.use('Qt5Agg')

# Define Your Calculator


class Opreator(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout(self)
        self.setMinimumSize(600,300)
        self.LabelInput=QLabel("输入")
        self.LabelOutput=QLabel("结果")
        self.EditC=QLineEdit()
        self.EditRa=QLineEdit()
        self.EditRb=QLineEdit()
        self.LabelC=QLabel("C(F)")
        self.LabelRa=QLabel("Ra(Ω)")
        self.LabelRb=QLabel("Rb(Ω)")
        self.ShowDutyRate=QLineEdit()
        self.ShowFre=QLineEdit()
        self.LabelDutyRate=QLabel("占空比")
        self.LabelFre=QLabel("频率(Hz)")
        self.opbtn=QPushButton("计算")
        self.rstbtn=QPushButton("重置")
        self.layout.addWidget(self.LabelInput,0,0,2,1)
        self.layout.addWidget(self.LabelOutput,0,2,2,1)
        self.layout.addWidget(self.EditC,1,0)
        self.layout.addWidget(self.EditRa,2,0)
        self.layout.addWidget(self.EditRb,3,0)
        self.layout.addWidget(self.LabelC,1,1)
        self.layout.addWidget(self.LabelRa,2,1)
        self.layout.addWidget(self.LabelRb,3,1)
        self.layout.addWidget(self.ShowDutyRate,1,2)
        self.layout.addWidget(self.ShowFre,2,2)
        self.layout.addWidget(self.LabelDutyRate,1,3)
        self.layout.addWidget(self.LabelFre,2,3)
        self.layout.addWidget(self.opbtn,3,2)
        self.layout.addWidget(self.rstbtn,3,3)
        self.opbtn.clicked.connect(self.op)
        self.rstbtn.clicked.connect(self.rst)

    def rst(self):
        self.EditRa.setText("")
        self.EditC.setText("")
        self.EditRb.setText("")
        self.ShowDutyRate.setText("")
        self.ShowFre.setText("")

    def op(self):
        Ra=float(self.EditRa.text())
        Rb=float(self.EditRb.text())
        C=float(self.EditC.text())
        f=1.44 / ((Ra + Rb + Rb) * C)
        Th = 0.693 * (Ra + Rb) * C
        Tl = 0.693 * Rb * C
        Duty = (Th / (Th + Tl)) * 100
        self.ShowFre.setText(str(f))
        self.ShowDutyRate.setText(str(Duty))

        
class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.DrawNE555(), 0, 0, 2, 1)
        self.layout.setMargin(0)
        self.layout.setSpacing(0)
        self.OpWidget=Opreator()
        self.layout.addWidget(self.OpWidget)


    def DrawNE555(self):
        d = schemdraw.Drawing()
        IC555def = elm.Ic(pins=[elm.IcPin(name='TRG', side='left', pin='2'),
                                elm.IcPin(name='THR', side='left', pin='6'),
                                elm.IcPin(name='DIS', side='left', pin='7'),
                                elm.IcPin(name='CTL', side='right', pin='5'),
                                elm.IcPin(name='OUT', side='right', pin='3'),
                                elm.IcPin(name='RST', side='top', pin='4'),
                                elm.IcPin(name='Vcc', side='top', pin='8'),
                                elm.IcPin(name='GND', side='bot', pin='1'),],
                           edgepadW=.5,
                           edgepadH=1,
                           pinspacing=2,
                           leadlen=1,
                           label='555')
        T = d.add(IC555def)
        BOT = d.add(elm.Ground(xy=T.GND))
        d.add(elm.Dot)
        d.add(elm.Resistor(endpts=[T.DIS, T.THR], label='Rb'))
        d.add(elm.Resistor('u', xy=T.DIS, label='Ra', rgtlabel='+Vcc'))
        d.add(elm.Line(endpts=[T.THR, T.TRG]))
        d.add(elm.Capacitor('d', xy=T.TRG, toy=BOT.start, label='C', l=d.unit/2))
        d.add(elm.Line('r', tox=BOT.start))
        d.add(elm.Capacitor('d', xy=T.CTL, toy=BOT.start, botlabel='.01$\mu$F'))
        d.add(elm.Dot(xy=T.DIS))
        d.add(elm.Dot(xy=T.THR))
        d.add(elm.Dot(xy=T.TRG))
        d.add(elm.Line(endpts=[T.RST,T.Vcc]))
        d.add(elm.Dot)
        d.add(elm.Line('u', l=d.unit/4, rgtlabel='+Vcc'))
        d.add(elm.Resistor('r', xy=T.OUT, label='330'))
        d.add(elm.LED(flip=True, d='down', toy=BOT.start))
        d.add(elm.Line('l', tox=BOT.start))
        return FigureCanvas(d.draw(show=False).getfig())


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
