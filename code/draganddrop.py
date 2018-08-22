#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#### Some code to work with drag and drop functionality ####

# class Button(QPushButton):
  
#     def __init__(self, title, parent):
#         super().__init__(title, parent)
        
#         self.setAcceptDrops(True)
        

#     def dragEnterEvent(self, e):
      
#         if e.mimeData().hasFormat('text/plain'):
#             e.accept()
#         else:
#             e.ignore() Í

#     def dropEvent(self, e):
        
#         self.setText(e.mimeData().text()) 


class Example(QWidget):
  
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        label1 = QLabel(self)
        label1.setText("Drag")
        label1.move(130, 40)

        label2 = QLabel(self)
        label2.setText("A")
        label2.move(140, 65)

        label3 = QLabel(self)
        label3.setText("File")
        label3.move(135, 90)
        
        self.setWindowTitle('IsoType')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
  
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()  