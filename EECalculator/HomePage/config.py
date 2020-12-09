#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtGui import QFont
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel
from PySide2.QtCore import Qt, QSize, QMargins

class MenuFont(QFont):
    def __init__(self):
        QFont.__init__(self)
        self.setPointSize(20)


class DisplayFont(QFont):
    def __init__(self):
        QFont.__init__(self)
        self.setPointSize(20)
#TODO:change "Dark" and "Light" Theme
class SettingWdiget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

