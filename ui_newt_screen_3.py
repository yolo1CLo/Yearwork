from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.m_DSB = QDoubleSpinBox(Form)
        self.m_DSB.setObjectName(u"doubleSpinBox")
        self.m_DSB.setGeometry(QRect(30, 140, 62, 24))
        self.a_DSB = QDoubleSpinBox(Form)
        self.a_DSB.setObjectName(u"doubleSpinBox_2")
        self.a_DSB.setGeometry(QRect(160, 140, 62, 24))
        self.F_DSB = QDoubleSpinBox(Form)
        self.F_DSB.setObjectName(u"doubleSpinBox_3")
        self.F_DSB.setGeometry(QRect(280, 140, 62, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 251, 61))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 101, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 80, 131, 51))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 90, 101, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 260, 80, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 170, 80, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Here you can calculate the Newton Force", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Input for masse", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Input for acceleration", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Input for Force", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
    # retranslateUi

