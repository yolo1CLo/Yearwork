from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.S_DSB = QDoubleSpinBox(Form)
        self.S_DSB.setObjectName(u"doubleSpinBox_3")
        self.S_DSB.setGeometry(QRect(290, 170, 62, 24))
        self.d_DSB = QDoubleSpinBox(Form)
        self.d_DSB.setObjectName(u"doubleSpinBox")
        self.d_DSB.setGeometry(QRect(40, 170, 62, 24))
        self.t_DSB = QDoubleSpinBox(Form)
        self.t_DSB.setObjectName(u"doubleSpinBox_2")
        self.t_DSB.setGeometry(QRect(170, 170, 62, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 251, 61))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 120, 111, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 120, 101, 31))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 120, 101, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 270, 80, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 220, 80, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Here you can calculate the Speed", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Input for distance", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Input for time", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Input for speed", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
    # retranslateUi

