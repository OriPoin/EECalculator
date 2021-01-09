#!/usr/bin/env python
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout
from PySide2.QtCore import Qt, QSize, QMargins

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # generate the plot
    fig = Figure(figsize=(600,600), dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
    ax = fig.add_subplot(111)
    ax.plot([0,1])
    # generate the canvas to display the plot
    canvas = FigureCanvas(fig)

    win = QMainWindow()
    # add the plot canvas to a window
    win.setCentralWidget(canvas)

    win.show()

    sys.exit(app.exec_())