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

sys.path.append("../EECalculator")
from EECalculator.HomePage import homepage, config


def CleanWidgets(Parent):
    while Parent.count():
        Child = Parent.takeAt(0)
        if Child.widget():
            Child.widget().deleteLater()


def GetMenuList(Path, MenuListLayout, Width, Height):
    ModuleWidget = []
    ModuleList = []
    i = 0
    for module in os.listdir(Path):
        if os.path.isdir(os.path.join(Path, module)) and module != "__pycache__":
            ModuleList.append(module)
            ModuleWidget.append(QPushButton(module))
            ModuleWidget[i].setFixedWidth(Width)
            ModuleWidget[i].setFixedHeight(Height)
            MenuListLayout.addWidget(ModuleWidget[i])
            i += 1
    MenuListLayout.addStretch(1)


class EECalculator(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self)
        # TODO:use framelesswindow
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.PackagePath = "EECalculator"
        self.InitUI()

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

        # Setup Widget&LAyout
        self.MenuScrollArea.setFixedWidth(200)
        self.MenuScrollAreaLayout.setMargin(0)
        self.MenuScrollAreaLayout.setSpacing(0)
        self.DisplayLayout.setMargin(0)
        self.MainLayout.setMargin(0)
        self.MenuScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MenuScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        GetMenuList(self.PackagePath, self.MenuScrollAreaLayout, 198, 66)
        self.MenuScrollArea.setWidget(self.MenuScrollAreaContents)

        self.DisplayWidget = homepage.MainWidget()

        self.MainLayout.addWidget(self.DisplayWidget)
        self.MainLayout.addWidget(self.MenuScrollArea)
        self.MainLayout.addWidget(self.DisplayWidget)
        self.setCentralWidget(self.MainWidget)


class CalculatorAPP(QApplication):
    def __init__(self, arg__1):
        super().__init__(arg__1)
        self.setStyle("Fusion")
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
