#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtCore import Qt, QSize, QMargins
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QVBoxLayout,
    QScrollArea,
    QHBoxLayout,
    QLabel,
)
import os
import sys
from functools import partial

sys.path.append("../EECalculator")
from EECalculator.HomePage import homepage, config
from EECalculator.RCFilter import rc
from EECalculator.TcOfCap import tcap
from EECalculator.NE555 import ne555

modules = ['Home','RC Filter','Capacitor discharge','NE555']

class EECalculator(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        # TODO:use framelesswindow
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.InitUI()

    def RefreshWidgets(self,target,name):
        while target.count():
            Child = target.takeAt(0)
            if Child.widget():
                Child.widget().deleteLater()
        if name==modules[0]:
            target.addWidget(homepage.MainWidget())
        if name==modules[1]:
            target.addWidget(rc.MainWidget())
        if name==modules[2]:
            target.addWidget(tcap.MainWidget())
        if name==modules[3]:
            target.addWidget(ne555.MainWidget())
            
        
    def InitUI(self):
        # Set Window Size
        self.resize(800, 600)
        self.setMinimumSize(QSize(800, 600))
        # Set Window Titile
        self.setWindowTitle("EE Calculator")

        # Create Main Widgets
        self.MainWidget = QWidget()
        self.MainLayout = QHBoxLayout(self.MainWidget)
        # Create Display Widgets
        self.DisplayWidget = QWidget(self.MainWidget)
        self.DisplayLayout = QGridLayout(self.DisplayWidget)
        # Create Menu Area&Widgets
        self.MenuScrollArea = QScrollArea(self.MainWidget)
        self.MenuScrollAreaContents = QWidget()
        self.MenuScrollAreaLayout = QVBoxLayout(self.MenuScrollAreaContents)

        ButtonList=[]
        i = 0
        for module in modules:
            ButtonList.append(QPushButton(module))
            ButtonList[i].setFixedWidth(198)
            ButtonList[i].setFixedHeight(66)
            ButtonList[i].clicked.connect(partial(self.RefreshWidgets,self.DisplayLayout,module))
            self.MenuScrollAreaLayout.addWidget(ButtonList[i])
            i += 1
        self.MenuScrollAreaLayout.addStretch(1)

        # Setup Widget&LAyout
        self.MenuScrollArea.setFixedWidth(200)
        self.MenuScrollAreaLayout.setMargin(0)
        self.MenuScrollAreaLayout.setSpacing(0)
        self.DisplayLayout.setMargin(0)
        self.MainLayout.setMargin(0)
        self.MenuScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MenuScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MenuScrollArea.setWidget(self.MenuScrollAreaContents)

        self.DisplayLayout.addWidget(homepage.MainWidget())

        self.MainLayout.addWidget(self.MenuScrollArea)
        self.MainLayout.addWidget(self.DisplayWidget)
        self.setCentralWidget(self.MainWidget)


class CalculatorAPP(QApplication):
    def __init__(self, arg__1):
        super().__init__(arg__1)
        self.setStyle("Fusion")
        # self.setStyle('Windows')
        self.Window = EECalculator(self)
        self.Window.show()


if __name__ == "__main__":
    app = CalculatorAPP([])
    sys.exit(app.exec_())
#
#         ┌─┐       ┌─┐
#      ┌──┘ ┴───────┘ ┴──┐
#      │                 │
#      │       ──        │
#      │  ＞         ＜  │
#      │                 │
#      │   ..  ⌒  ..    │
#      │                 │
#      └───┐         ┌───┘
#          │         │
#          │         │
#          │         │
#          │         └──────────────┐
#          │                        │
#          │                        ├─┐
#          │                        ┌─┘
#          │                        │
#          └─┐  ┐  ┌───────┬──┐  ┌──┘
#            │ ─┤ ─┤       │ ─┤ ─┤
#            └──┴──┘       └──┴──┘
#       Codes are far away from bugs with the caonima protecting
#       神兽保佑,代码无BUG!
