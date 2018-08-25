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


class App(QMainWindow):
  
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    ######Code for file explorer for manual import features
    # def openFileNameDialog(self):    
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
    #     if fileName:
    #         print(fileName)
 
    # def openFileNamesDialog(self):    
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
    #     if files:
    #         print(files)
 
    # def saveFileDialog(self):    
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #     if fileName:
    #         print(fileName)
        
    def initUI(self):

        self.setWindowTitle('IsoType')
        self.setGeometry(500, 250, 800, 600)

        backlabel = QLabel(self)
        pixmap = QPixmap('../images/background-1.png')
        backlabel.setPixmap(pixmap)

        label1 = QLabel(self)
        label1.setText("Drag")
        label1.move(380, 200)

        label2 = QLabel(self)
        label2.setText("A")
        label2.move(390, 240)

        label3 = QLabel(self)
        label3.setText("File")
        label3.move(385, 280)

        message = "Awaiting file..."
        self.statusBar().showMessage(message)

        #####Code for import window
        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()

        self.show()


if __name__ == '__main__':
  
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()  