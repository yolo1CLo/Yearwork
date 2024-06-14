from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox
import sys
import matplotlib.pyplot as plt
import ui_quad_screen_2, ui_newt_mass_7, ui_work_screen_4, ui_calc_screen_1, ui_kine_screen_6, ui_speed_screen_5, ui_newt_home_3
import ui_newt_acceleration_8, ui_newt_force_9, ui_work_D_10, ui_work_W_12, ui_work_F_11, ui_speed_distance_13, ui_speed_speed_15, ui_speed_time_14
import ui_kin_E_18, ui_kin_m_16, ui_kin_s_17
from ui_calc_screen_1 import Ui_MainWindow
from ui_quad_screen_2 import Ui_Form
from ui_newt_mass_7 import Ui_Form
from ui_work_screen_4 import Ui_Form
from ui_speed_screen_5 import Ui_Form
from ui_work_screen_4 import Ui_Form
from ui_newt_home_3 import Ui_Form
from ui_newt_acceleration_8 import Ui_Form
from ui_newt_force_9 import Ui_Form
from ui_work_F_11 import Ui_Form
from ui_work_W_12 import Ui_Form
from ui_work_D_10 import Ui_Form
from ui_speed_distance_13 import Ui_Form
from ui_speed_time_14 import Ui_Form
from ui_speed_speed_15 import Ui_Form
from ui_kin_m_16 import Ui_Form
from ui_kin_s_17 import Ui_Form
from ui_kin_E_18 import Ui_Form
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
        self.result = self.ui.resultLabel.setText('Here the result will be displayed')
        self.a = self.ui.a_DSB.value()
        self.F = self.ui.f_DSB.value()
        self.ui.a_DSB.valueChanged.connect(self.calcNewton)
        self.ui.f_DSB.valueChanged.connect(self.calcNewton) 
    
    def calcNewton (self):
        self.a = self.ui.a_DSB.value()
        self.F = self.ui.f_DSB.value()
        try: 
            self.m = self.F/self.a
            self.ui.resultLabel.setText(f"The value of {self.F} divided by {self.a} is equal to the m being {self.m} kg.")
            return self.m
        except ZeroDivisionError:
            print("Can't divide by zero")

class Newt_acceleration (QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_acceleration, self).__init__()
        self.ui = ui_newt_acceleration_8.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.m = self.ui.m_DSB.value()
        self.F = self.ui.f_DSB.value()
        self.ui.m_DSB.valueChanged.connect(self.calcNewton)
        self.ui.f_DSB.valueChanged.connect(self.calcNewton) 

    def calcNewton (self):
        self.m = self.ui.m_DSB.value()
        self.F = self.ui.f_DSB.value()
        try: 
            a = self.F/self.m
            self.ui.resultLabel.setText(f"The value of {self.F} divided by {self.m} is equal to the m being {a} kg.")
            return self.m
        except ZeroDivisionError:
            print("Can't divide by zero")

class Newt_force(QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_force, self).__init__()
        self.ui = ui_newt_force_9.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.m = self.ui.m_DSB.value()
        self.a = self.ui.a_DSB.value()
        self.ui.m_DSB.valueChanged.connect(self.calcNewton)
        self.ui.a_DSB.valueChanged.connect(self.calcNewton) 

    def calcNewton (self):
        self.m = self.ui.m_DSB.value()
        self.a = self.ui.a_DSB.value()
        try: 
            self.F = self.m*self.a
            self.ui.resultLabel.setText(f"The value of the Force is {self.F}")
            return self.F
        except ZeroDivisionError:
            print("Can't divide by zero")

class Work_homepage(QMainWindow):
    def __init__(self, stackWidget):
        super(Work_homepage, self).__init__()
        self.ui = ui_work_screen_4.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.pushButton.clicked.connect (self.Return)
        self.ui.pushButton_2.clicked.connect (self.gotoWo_D)
        self.ui.pushButton_3.clicked.connect (self.gotoWo_F)
        self.ui.pushButton_4.clicked.connect (self.gotoWo_W)
    
    def gotoWo_D (self):
        self.stackWidget.setCurrentIndex (10)
    def gotoWo_F (self):
        self.stackWidget.setCurrentIndex (11)
    def gotoWo_W (self):
        self.stackWidget.setCurrentIndex (12)
    def Return (self):
        self.stackWidget.setCurrentIndex (1)

class Work_D (QMainWindow):
    def __init__(self, stackWidget):
        super(Work_D, self).__init__()
        self.ui = ui_work_D_10.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.F = self.ui.F_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.w = self.ui.w_DSB.value()
        self.ui.F_DSB.valueChanged.connect(self.calcWork)
        self.ui.c_DSB.valueChanged.connect(self.calcWork) 
        self.ui.w_DSB.valueChanged.connect(self.calcWork)
        
    def calcWork (self):
        try:
            self.d = self.c/(math.cos(self.c)*self.F)
            print (f"The value of the distance is equal too {self.d}")                 
            return self.d
        except ZeroDivisionError:
            print("Error: Division by zero. ")

class Work_W (QMainWindow):
    def __init__(self, stackWidget):
        super(Work_W, self).__init__()
        self.ui = ui_work_W_12.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.d = self.ui.d_DSB.value()
        self.F = self.ui.F_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.ui.F_DSB.valueChanged.connect(self.calcWork)
        self.ui.c_DSB.valueChanged.connect(self.calcWork) 
        self.ui.d_DSB.valueChanged.connect(self.calcWork)
        
    def calcWork (self):
        self.W = self.F * self.d * math.cos(self.c)
        self.ui.resultLabel.setText(f"The Work for this calculus is equal too {self.W}J")
        return self.W     

class Work_F (QMainWindow):
    def __init__(self, stackWidget):
        super(Work_F, self).__init__()
        self.ui = ui_work_F_11.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.d = self.ui.d_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.W = self.ui.W_DSB.value()
        self.ui.W_DSB.valueChanged.connect(self.calcWork)
        self.ui.c_DSB.valueChanged.connect(self.calcWork) 
        self.ui.d_DSB.valueChanged.connect(self.calcWork)
        self.ui.pushButton.clicked.connect(self.Return)

        
    def calcWork (self):
        try:
            self.F = self.W/self.d.math.cos(self.c)
            self.ui.resultLabel.setText(f"The Fore is equal too {self.F}N")
            return self.F
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

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
        self.stackWidget = stackWidget

        self.ui.pushButton.clicked.connect(self.Return)
        self.ui.pushButton_2.clicked.connect (self.gotospeed_distance)
        self.ui.pushButton_3.clicked.connect (self.gotospeed_time)
        self.ui.pushButton_4.clicked.connect (self.gotospeed_speed)

    def gotospeed_distance(self):
        self.stackWidget.setCurrentIndex (13)
    def gotospeed_time(self):
        self.stackWidget.setCurrentIndex (14)
    def gotospeed_speed(self):
        self.stackWidget.setCurrentIndex (15)
    def Return(self):
        self.stackWidget.setCurrentIndex (5)

class Speed_distance (QMainWindow):
    def __init__(self, stackWidget):
        super(Speed_distance, self).__init__()
        self.ui = ui_speed_distance_13.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.t = self.ui.t_DSB.value()
        self.s = self.ui.s_DSB.value()
        self.ui.t_DSB.valueChanged.connect(self.calcSpeed) 
        self.ui.s_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.pushButton.clicked.connect(self.Return)

    def calcSpeed (self):
        try:
            self.d = self.t/self.s
            self.ui.resultLabel.setText(f"The distance is equal too {self.d}")
            return self.d
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

class Speed_time (QMainWindow):
    def __init__(self, stackWidget):
        super(Speed_time, self).__init__()
        self.ui = ui_speed_time_14.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.d_DSB.valueChanged.connect(self.calcSpeed) 
        self.ui.s_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.pushButton.clicked.connect(self.Return)


    def calcSpeed (self):
        try:
            self.t = self.s * self.d
            self.ui.resultLabel.setText(f"The time is equal too {self.t}")
            return self.t
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

class Speed_speed (QMainWindow):
    def __init__(self, stackWidget):
        super(Speed_speed, self).__init__()
        self.ui = ui_speed_speed_15.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.t_DSB.valueChanged.connect(self.calcSpeed) 
        self.ui.d_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.pushButton.clicked.connect(self.Return)


    def calcSpeed (self):
        try:
            self.s = self.d/self.t
            self.ui.resultLabel.setText(f"The speed is equal too {self.s}")
            return self.s
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

class Kinetic (QMainWindow):
    def __init__(self, stackWidget):
        super(Kinetic, self).__init__()
        self.ui = ui_kine_screen_6.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.ui.pushButton.clicked.connect(self.Return)
        self.ui.pushButton_2.clicked.connect (self.gotokin_mass)
        self.ui.pushButton_3.clicked.connect (self.gotokin_speed)
        self.ui.pushButton_4.clicked.connect (self.gotokin_energy)

    def gotokin_mass(self):
        self.stackWidget.setCurrentIndex (16)
    def gotokin_speed(self):
        self.stackWidget.setCurrentIndex (17)
    def gotokin_energy(self):
        self.stackWidget.setCurrentIndex (18)
    def Return(self):
        self.stackWidget.setCurrentIndex (1)

class Kine_mass (QMainWindow):
    def __init__(self, stackWidget):
        super(Kine_mass, self).__init__()
        self.ui = ui_kin_m_16.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
         
        self.ui.e_DSB.valueChanged.connect(self.calcKine) 
        self.ui.s_DSB.valueChanged.connect(self.calcKine)
        self.ui.pushButton.clicked.connect(self.Return)


    def calcKine (self):
        c = 0.5
        try:
            self.m = self.K/(self.S**2) * c
            self.ui.resultLabel.setText(f"The value of the mass is equal to {self.m}.")
            return self.m
        except ZeroDivisionError:
            print("Error: Division by zero. ")

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

class Kine_speed (QMainWindow):
    def __init__(self, stackWidget):
        super(Kine_speed, self).__init__()
        self.ui = ui_kin_s_17.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.e_DSB.valueChanged.connect(self.calcKine) 
        self.ui.m_DSB.valueChanged.connect(self.calcKine)
        self.ui.pushButton.clicked.connect(self.Return)

    def calcKine (self):
        c = 0.5
        try:
            self.S = math.sqrt(self.K/c*self.m)
            self.ui.reslabel.setText(f"The value of the speed is equal to {self.v}")
            return self.S
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Error: Division by zero.")

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

class Kine_kine (QMainWindow):
    def __init__(self, stackWidget):
        super(Kine_kine, self).__init__()
        self.ui = ui_kin_E_18.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.S_DSB.valueChanged.connect(self.calcKine) 
        self.ui.m_DSB.valueChanged.connect(self.calcKine)
        self.ui.pushButton.clicked.connect(self.Return)

    def calcKine (self):
        c = 0.5
        self.K =  self.c* self.S**2 * self.m
        self.ui.resultLabel.setText(f"The Kinetic Energy is equal to {self.K}N")
        return self.K

    def Return (self):
        self.stackWidget.setCurrentIndex (1)

def main():
    app = QApplication(sys.argv) #QWidget: Must construct a QApplication before a QWidget
    stackWidget = QtWidgets.QStackedWidget()  # Centralized QStackedWidget
    main_window = MyWindow(stackWidget)
    calc_window = Calc(stackWidget)
    quadr_window = Quadratic(stackWidget)
    newt_window = Newton_homepage(stackWidget)
    work_window = Work_homepage(stackWidget)
    speed_window = Speed(stackWidget)
    kine_window = Kinetic(stackWidget)
    newt__window_m = Newt_mass(stackWidget)
    newt__window_a = Newt_acceleration(stackWidget)
    newt__window_F = Newt_force(stackWidget)
    work_window_d = Work_D (stackWidget)
    work_window_w = Work_W (stackWidget)
    work_window_f = Work_F (stackWidget)
    speed_window_d = Speed_distance (stackWidget)
    speed_window_t = Speed_time(stackWidget)
    speed_window_s = Speed_speed (stackWidget)
    kine_window_m = Kine_mass(stackWidget)
    kine_window_s = Kine_speed(stackWidget)
    kine_window_k = Kine_kine(stackWidget)

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
    stackWidget.addWidget (work_window_d)
    stackWidget.addWidget (work_window_f)
    stackWidget.addWidget (work_window_w)
    stackWidget.addWidget (speed_window_d)
    stackWidget.addWidget (speed_window_t)
    stackWidget.addWidget (speed_window_s)
    stackWidget.addWidget (kine_window_m)
    stackWidget.addWidget (kine_window_s)
    stackWidget.addWidget (kine_window_k)

    stackWidget.setCurrentIndex(0)  # Show mainwindow first
    stackWidget.show()  # Show the stackWidget
    
    sys.exit(app.exec_())

main()