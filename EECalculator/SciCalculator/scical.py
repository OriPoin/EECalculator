#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton,QLineEdit
from PySide2.QtCore import Qt, QSize, QMargins

sys.path.append('../EECalculator')
from EECalculator.HomePage import config


# Define Your Calculator

class ResultSubWidget(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.layout=QGridLayout(self)
        self.InWidget=QLineEdit(self)
        self.OutWidget=QLabel(self)
        self.layout.addWidget(self.InWidget,0,0,8,1)
        self.layout.addWidget(self.OutWidget,0,0,2,1)
    
class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.MainLayout=QGridLayout(self)

    def SetupUI(self):
        # Create Widgets and Buttons
        self.ResultWidget=[6]

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