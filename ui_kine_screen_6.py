from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 40, 261, 61))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 120, 101, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 120, 101, 31))
        self.E_DSB = QDoubleSpinBox(Form)
        self.E_DSB.setObjectName(u"doubleSpinBox_3")
        self.E_DSB.setGeometry(QRect(300, 170, 62, 24))
        self.S_DSB = QDoubleSpinBox(Form)
        self.S_DSB.setObjectName(u"doubleSpinBox")
        self.S_DSB.setGeometry(QRect(50, 170, 62, 24))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 111, 31))
        self.m_DSB= QDoubleSpinBox(Form)
        self.m_DSB.setObjectName(u"doubleSpinBox_2")
        self.m_DSB.setGeometry(QRect(180, 170, 62, 24))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 260, 80, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 210, 80, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Here you can calculate the Kinetic Energy", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Input for Energy", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Input for mass", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Input for speed", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
    # retranslateUi

