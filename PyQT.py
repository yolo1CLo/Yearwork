from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow (QMainWindow):
    def __init__ (self,app):
        super(MyWindow, self). __init__()
        uic.loadUi('GUI/screen1.ui', self)

        self.app = app
        self.stackWidget = QtWidgets.QStackedWidget() # Create a single QStackedWidget

        self.pushButton.clicked.connect(self.gotocalc)

    def gotocalc(self):
        self.stackWidget.setCurrentIndex(1) # Show mainwindow first
        self.stackWidget.show() # Show the stackWidget

class calc (QMainWindow):
    def __init__ (self,app):
        super(calc, self). __init__()
        uic.loadUi('GUI/screen2.ui', self)

        self.app = app
        self.stackWidget = QtWidgets.QStackedWidget() # Create a single QStackedWidget

        self.pushButton_1.clicked.connect(self.goto_quadratic)
   
    def goto_quadratic(self):
        self.stackWidget.setCurrentIndex(2) 
        self.stackWidget.show()

class quadratic (QMainWindow):
    def __init__ (self):
        super(quadratic, self). __init__()
        uic.loadUi('GUI/quadratic.ui', self)

def window():
    app = QApplication(sys.argv)
    
    mainwindow = MyWindow(app)
    screen2 = calc() # Assuming you want to initialize this at the start
    screen3 = quadratic()

    mainwindow.stackWidget.addWidget(mainwindow) # Add mainwindow
    mainwindow.stackWidget.addWidget(screen2) # Add screen2
    mainwindow.stackWidget.addWidget(screen3) # Add screen3
    mainwindow.stackWidget.setCurrentIndex(0) # Show mainwindow first
    mainwindow.stackWidget.show() # Show the stackWidget
    
    sys.exit(mainwindow.app.exec_())
window()        
