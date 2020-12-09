#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide2.QtCore import Qt, QSize, QMargins

sys.path.append("../EECalculator")
from EECalculator.HomePage import config

# Claculator Class
class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.MainLayout = QVBoxLayout(self)
        self.InitUI()

    def InitUI(self):
        self.Title = QLabel("EE Claculator\n A set of Calculators for EE")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Title.setFont(config.MenuFont())
        self.MainLayout.addWidget(self.Title)


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
