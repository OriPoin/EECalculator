# # Test Window
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# import sys
# from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
# from PySide2.QtCore import Qt, QSize, QMargins

# sys.path.append('../EECalculator')
# from EECalculator.HomePage import config


# # Define Your Calculator
# class MainWidget(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)


# # Test Window
# class Calculator(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.MainWidget = MainWidget()
#         self.SetupWindow()

#     def SetupWindow(self):
#         # Set Window Size
#         self.resize(600, 600)
#         self.setMinimumSize(QSize(600, 600))
#         # Set Window Titile
#         self.setWindowTitle(type(self.MainWidget).__name__)
#         self.setCentralWidget(self.MainWidget)


# if __name__ == "__main__":
#     app = QApplication([])
#     app.setStyle("Fusion")
#     window = Calculator()
#     window.show()
#     sys.exit(app.exec_())

import numpy as np
import matplotlib.pyplot as plt


# Example data
t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4 * np.pi * t) + 2

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(t, s)

plt.xlabel(r'\textbf{time} (s)')
plt.ylabel(r'\textit{voltage} (mV)',fontsize=16)
plt.title(r"\TeX\ is Number "
          r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
          fontsize=16, color='gray')
# Make room for the ridiculously large title.
plt.subplots_adjust(top=0.8)

plt.savefig('tex_demo')
plt.show()