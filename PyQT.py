from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox
import sys
import matplotlib.pyplot as plt
import ui_quad_screen_2, ui_newt_mass_7, ui_work_screen_4, ui_calc_screen_1, ui_kine_screen_6, ui_speed_screen_5, ui_newt_home_3
import ui_newt_acceleration_8, ui_newt_force_9
from ui_calc_screen_1 import Ui_MainWindow
from ui_quad_screen_2 import Ui_Form
from ui_newt_mass_7 import Ui_Form
from ui_work_screen_4 import Ui_Form
from ui_speed_screen_5 import Ui_Form
from ui_work_screen_4 import Ui_Form
from ui_newt_home_3 import Ui_Form
from ui_newt_acceleration_8 import Ui_Form
from ui_newt_force_9 import Ui_Form
import math

class MyWindow(QMainWindow):
    def __init__(self, stackWidget):
        super(MyWindow, self).__init__()
        uic.loadUi('main_screen_0.ui', self)  # Load the screen.ui file parameters
        self.stackWidget = stackWidget
        self.pushButton.clicked.connect(self.gotoCalc)  # Assuming pushButton exists in screen1.ui
        self.graph = Graph()
        self.pushButton_2.clicked.connect (self.graph.generate_graph)

    def gotoCalc(self):
        self.stackWidget.setCurrentIndex(1)

class Calc(QMainWindow):
    def __init__(self, stackWidget):
        super(Calc, self).__init__()
        self.ui = ui_calc_screen_1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.pushButton_2.clicked.connect(self.Return)
        self.ui.pushButton_1.clicked.connect (self.gotoQuadratic)
        self.ui.pushButton_3.clicked.connect (self.gotoNewt)
        self.ui.pushButton_4.clicked.connect (self.gotoWork)
        self.ui.pushButton_5.clicked.connect (self.gotoSpeed)
        self.ui.pushButton.clicked.connect (self.gotoKine)
  
    def gotoNewt(self):
        self.stackWidget.setCurrentIndex (3)
    def gotoWork (self):
        self.stackWidget.setCurrentIndex (4)
    def gotoQuadratic(self):
        self.stackWidget.setCurrentIndex(2)
    def gotoSpeed(self):
        self.stackWidget.setCurrentIndex(5)
    def gotoKine (self):
        self.stackWidget.setCurrentIndex(6)
    def Return (self):
        self.stackWidget.setCurrentIndex (0)

class Quadratic(QMainWindow):
    def __init__(self, stackWidget):
        super(Quadratic, self).__init__()
        self.ui = ui_quad_screen_2.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.a = self.ui.a_DSB.value()
        self.b = self.ui.b_DSB.value()
        self.c = self.ui.c_DSB.value()

        self.ui.pushButton.clicked.connect (self.Return)
        self.result = self.ui.resultLabel.setText('Here the result will be displayed')
        
        self.ui.a_DSB.valueChanged.connect(self.calcQuad)
        self.ui.b_DSB.valueChanged.connect(self.calcQuad)
        self.ui.c_DSB.valueChanged.connect(self.calcQuad)

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

    def calcQuad(self):
        self.a = self.ui.a_DSB.value()
        self.b = self.ui.b_DSB.value()
        self.c = self.ui.c_DSB.value()
        discriminant = self.b**2 - 4*self.a*self.c
        if self.a !=0:
            if discriminant < 0:
                self.ui.resultLabel.setText("The Discriminant is inferior to zero.")
                return None  
            elif discriminant == 0:
                x = (-self.b) / (2*self.a)
                self.ui.resultLabel.setText(f"x: {x}")
            else:
                x1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
                x2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)
                self.ui.resultLabel.setText(f"x1: {x1} andx2: {x2}")
        else:
            self.ui.resultLabel.setText("Can't divide by 0")

class Newton_homepage(QMainWindow):
    def __init__(self, stackWidget):
        super(Newton_homepage, self).__init__()
        self.ui = ui_newt_home_3.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.pushButton_4.clicked.connect(self.Return)
        self.ui.pushButton_1.clicked.connect (self.gotoNewt_mass)
        self.ui.pushButton_2.clicked.connect (self.gotoNewt_acceleration)
        self.ui.pushButton_3.clicked.connect (self.gotoNewt_force)

    def gotoNewt_mass(self):
        self.stackWidget.setCurrentIndex (7)
    def gotoNewt_acceleration(self):
        self.stackWidget.setCurrentIndex (8)
    def gotoNewt_force(self):
        self.stackWidget.setCurrentIndex (9)
    def Return(self):
        self.stackWidget.setCurrentIndex (3)

class Newt_mass (QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_mass, self).__init__()
        self.ui = ui_newt_mass_7.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

class Newt_acceleration (QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_acceleration, self).__init__()
        self.ui = ui_newt_acceleration_8.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

class Newt_force(QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_force, self).__init__()
        self.ui = ui_newt_force_9.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

class Work(QMainWindow):
    def __init__(self, stackWidget):
        super(Work, self).__init__()
        self.ui = ui_work_screen_4.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.d = self.ui.d_DSB.value()
        self.F = self.ui.F_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.W = self.ui.W_DSB

        self.ui.pushButton.clicked.connect (self.Return)
        self.ui.W_DSB.valueChanged.connect(self.calcWork)
        self.ui.d_DSB.valueChanged.connect(self.calcWork)
        self.ui.F_DSB.valueChanged.connect(self.calcWork) 
        self.result = self.ui.resultLabel.setText('Here the result will be displayed')

    def Return (self):
        self.stackWidget.setCurrentIndex (1)
    def calcWork (self):
        self.W = self.ui.W_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.F = self.ui.F_DSB.value()
        if self.d is None:
            try:
                self.d = self.W/math.cos(self.c)*self.F
                print (f"The value of the distance is equal too {self.d}")
                return self.d
            except ZeroDivisionError:
                print("Error: Division by zero. ")
        elif self.F is None:
            try:
                self.F = self.W/self.d.math.cos(self.c)
                self.ui.resultLabel.setText(f"The Fore is equal too {self.F}N")
                return self.F
            except ZeroDivisionError:
                print("Error: Division by zero.")
        elif self.c is None:
            try:
                self.c = self.W/self.d*self.F
                self.ui.resultLabel.setText(f"The value of the angle is equal too {self.c}.")
                return self.c
            except ZeroDivisionError:
                print("Error: Division by zero. ")
        else: 
            self.W = self.F * self.d * math.cos(self.c)
            self.ui.resultLabel.setText(f"The Work for this calculus is equal too {self.W}J")
            return UserWarning

class Graph(QMainWindow):
    def __init__(self):
        super(Graph,self ).__init__()

        self.setWindowTitle("Graph Generator")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.x_label = QLabel("Enter X Values:")
        self.layout.addWidget(self.x_label)
        self.x_entries = []
        self.y_label = QLabel("Enter Y Values:")
        self.layout.addWidget(self.y_label)
        self.y_entries = []

        for i in range(5):  # Adjust the range as per your requirement
            x_entry = QLineEdit()
            self.layout.addWidget(x_entry)
            self.x_entries.append(x_entry)

            y_entry = QLineEdit()
            self.layout.addWidget(y_entry)
            self.y_entries.append(y_entry)

        self.generate_button = QPushButton("Generate Graph")
        self.generate_button.clicked.connect(self.generate_graph)
        self.layout.addWidget(self.generate_button)

    def generate_graph(self):
        try:
            x_values = [float(x_entry.text()) for x_entry in self.x_entries if x_entry.text().strip()]
            y_values = [float(y_entry.text()) for y_entry in self.y_entries if y_entry.text().strip()]
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter valid numbers for all data points.")
            return

        if len(x_values) == 0 or len(y_values) == 0:
            QMessageBox.critical(self, "Error", "Please enter values for all data points.")
            return

        plt.plot(x_values, y_values)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Graph')
        plt.grid(True)
        plt.show()

class Speed (QMainWindow):
    def __init__(self, stackWidget):
        super(Speed, self).__init__()
        self.ui = ui_speed_screen_5.Ui_Form()
        self.ui.setupUi(self)
        self.result = self.ui.resultLabel.setText('Here the result will be displayed')

        self.t = self.ui.t_DSB.value()
        self.S = self.ui.S_DSB.value()
        self.d = self.ui.d_DSB.value()        
        
        self.stackWidget = stackWidget

        self.ui.pushButton.clicked.connect (self.Return)
        self.ui.S_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.t_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.d_DSB.valueChanged.connect(self.calcSpeed) 

    def Return (self):
        self.stackWidget.setCurrentIndex (1)
    def calcSpeed (self):
        self.S = self.ui.S_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.t = self.ui.t_DSB.value()        

        if self.d is None:
            self.d =  self.v* self.t
            self.ui.resultLabel.setText(f"The value of the distance is equal to { self.d}.")
            return  self.d
        elif self.t is None:
            try:
                self.t =  self.d/ self.v
                self.ui.resultLabel.setText(f"The value of the time is equal to {self.t}")
                return  self.t
            except ZeroDivisionError:
                self.ui.resultLabel.setText("Error: Division by zero. ")
        else: 
            try:
                self.v =  self.d / self.t
                self.ui.resultLabel.setText(f"The speed is equal to {self.v}m/s.")        
                return self.v
            except ZeroDivisionError:
                self.ui.resultLabel.setText("Error: Division by zero. ")

class Kinetic (QMainWindow):
    def __init__(self, stackWidget):
        super(Kinetic, self).__init__()
        self.ui = ui_kine_screen_6.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.result = self.ui.resultLabel.setText('Here the result will be displayed')

        self.m = self.ui.m_DSB.value()
        self.S = self.ui.S_DSB.value()
        self.E = self.ui.E_DSB.value()
        
        self.ui.pushButton.clicked.connect (self.Return)
        self.ui.E_DSB.valueChanged.connect(self.calcKinetic)
        self.ui.m_DSB.valueChanged.connect(self.calcKinetic)
        self.ui.S_DSB.valueChanged.connect(self.calcKinetic) 

    def Return (self):
        self.stackWidget.setCurrentIndex (1)
    def calcKinetic (self):
        self.m = self.ui.m_DSB.value()
        self.S = self.ui.S_DSB.value()
        self.E = self.ui.E_DSB.value()
        c = 0.5
        if self.m is None:
            try:
                self.m = self.K/(self.S**2) * c
                self.ui.resultLabel.setText(f"The value of the mass is equal to {self.m}.")
                return self.m
            except ZeroDivisionError:
                print("Error: Division by zero. ")
        elif self.S is None:
            try:
                self.S = math.sqrt(self.K/c*self.m)
                self.ui.resultLabel.setText(f"The value of the speed is equal to {self.v}")
                return self.S
            except ZeroDivisionError:
                self.ui.resultLabel.setText("Error: Division by zero.")
        else: 
            self.K =  self.c* self.S**2 * self.m
            self.ui.resultLabel.setText(f"The Kinetic Energy is equal to {self.K}N")
            return self.K

def main():
    app = QApplication(sys.argv) #QWidget: Must construct a QApplication before a QWidget
    stackWidget = QtWidgets.QStackedWidget()  # Centralized QStackedWidget
    
    # Create screen instances and pass the shared QStackedWidget to them
    main_window = MyWindow(stackWidget)
    calc_window = Calc(stackWidget)
    quadr_window = Quadratic(stackWidget)
    newt_window = Newton_homepage(stackWidget)
    work_window = Work(stackWidget)
    speed_window = Speed(stackWidget)
    kine_window = Kinetic(stackWidget)
    newt__window_m = Newt_mass(stackWidget)
    newt__window_a = Newt_acceleration(stackWidget)
    newt__window_F = Newt_force(stackWidget)
    # Add screens to the QStackedWidget
    stackWidget.addWidget(main_window)
    stackWidget.addWidget(calc_window)
    stackWidget.addWidget(quadr_window)
    stackWidget.addWidget (newt_window)
    stackWidget.addWidget(work_window)
    stackWidget.addWidget(speed_window)
    stackWidget.addWidget(kine_window)
    stackWidget.addWidget(newt__window_m)
    stackWidget.addWidget (newt__window_a)
    stackWidget.addWidget (newt__window_F)
    stackWidget.setCurrentIndex(0)  # Show mainwindow first
    stackWidget.show()  # Show the stackWidget
    
    sys.exit(app.exec_())

main()