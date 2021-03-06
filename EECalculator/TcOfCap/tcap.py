#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-12-24 18：31：45
# @Author  : j456maker (714642543@qq.com)
from PySide2 import QtWidgets, QtCore
class MainWidget(QtWidgets.QWidget):
     def __init__(self,parent=None):
          super().__init__(parent)
          self.label1=QtWidgets.QLabel("请输入您的值")
          self.label2=QtWidgets.QLabel("电容器两端的电压:V")
          self.line1=QtWidgets.QLineEdit()
          self.label3=QtWidgets.QLabel("Capacitance电容容量:uF")
          self.line2=QtWidgets.QLineEdit()
          self.label4=QtWidgets.QLabel("Load Resistance负载电阻:欧姆")
          self.line3=QtWidgets.QLineEdit()
          self.button_calc=QtWidgets.QPushButton("计算")
          self.button_clear=QtWidgets.QPushButton("清除")
          self.label5=QtWidgets.QLabel("结果：")
          self.label6=QtWidgets.QLabel("时间常数:秒seconds")
          self.line4=QtWidgets.QLineEdit()
          self.label7=QtWidgets.QLabel("Energy能量：")
          self.line5=QtWidgets.QLineEdit()
          self.label8=QtWidgets.QLabel("焦耳Joules")
          self.line6=QtWidgets.QLineEdit()
          self.label9=QtWidgets.QLabel("英制热量单位 BTU")
          self.layout = QtWidgets.QGridLayout()
          self.layout.addWidget(self.label1)
          self.layout.addWidget(self.label2)
          self.layout.addWidget(self.line1)
          self.layout.addWidget(self.label3)
          self.layout.addWidget(self.line2)
          self.layout.addWidget(self.label4)
          self.layout.addWidget(self.line3)
          self.layout.addWidget(self.button_calc)
          self.layout.addWidget(self.button_clear)
          self.layout.addWidget(self.label5)
          self.layout.addWidget(self.label6)
          self.layout.addWidget(self.line4)
          self.layout.addWidget(self.label7)
          self.layout.addWidget(self.line5)
          self.layout.addWidget(self.label8)
          self.layout.addWidget(self.line6)
          self.layout.addWidget(self.label9)
          self.setLayout(self.layout)
          self.button_calc.clicked.connect(self.calc1_timeconstant_energy)
          self.button_clear.clicked.connect(self.clear)

     def calc1_timeconstant_energy(self):
          str1=self.line1.text()
          a=float(str1)
          str2=self.line2.text()
          b=float(str2)
          str3=self.line3.text()
          c=float(str3)
          timeconstant = b*c*10**(-6)
          print(timeconstant)
          self.line4.setText(str(timeconstant))
          energy = 0.5*b*(a)**2*10**(-6)
          print(energy)
          self.line5.setText(str(energy))
          energy1=energy* 0.00094781712
          print(energy1)
          self.line6.setText(str(energy1))
     def clear(self):
          self.line1.clear()
          self.line2.clear()
          self.line3.clear()
          self.line4.clear()
          self.line5.clear()
          self.line6.clear()

     
          

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = MainWidget()
    layout = QtWidgets.QVBoxLayout()
    window.setLayout(layout)
    window.setMinimumSize(600,600)
    window.show()
    app.exec_()
