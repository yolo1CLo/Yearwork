from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox
import sys
import matplotlib.pyplot as plt

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
        uic.loadUi('calc_screen_1.ui', self)
        self.stackWidget = stackWidget
        self.pushButton_1.clicked.connect(self.gotoQuadratic)  # Assuming pushButton_1 exists in screen2.ui
    def gotoQuadratic(self):
        self.stackWidget.setCurrentIndex(2)

class Quadratic(QMainWindow):
    def __init__(self, stackWidget):
        super(Quadratic, self).__init__()
        uic.loadUi('quad_screen_2.ui', self)
        self.stackWidget = stackWidget
        # self.a_val = a_DSB.value()
        # self.b_val = b_DSB.value()
        # self.c_val = c_DSB.value()
    # def idk():
    #     answer = a.val * b.val()
        
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
        x_values = [float(x_entry.text()) for x_entry in self.x_entries]
        y_values = [float(y_entry.text()) for y_entry in self.y_entries]

        if not all(x_values) or not all(y_values):
            QMessageBox.critical(self, "Error", "Please enter values for all data points.")
            return

        plt.plot(x_values, y_values)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Graph')
        plt.grid(True)
        plt.show()

def main():
    app = QApplication(sys.argv) #QWidget: Must construct a QApplication before a QWidget
    stackWidget = QtWidgets.QStackedWidget()  # Centralized QStackedWidget
    
    # Create screen instances and pass the shared QStackedWidget to them
    main_window = MyWindow(stackWidget)
    calc_window = Calc(stackWidget)
    quadr_window = Quadratic(stackWidget)
    # Add screens to the QStackedWidget
    stackWidget.addWidget(main_window)
    stackWidget.addWidget(calc_window)
    stackWidget.addWidget(quadr_window)

    stackWidget.setCurrentIndex(0)  # Show mainwindow first
    stackWidget.show()  # Show the stackWidget
    
    sys.exit(app.exec_())

main()