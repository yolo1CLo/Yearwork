from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 110, 101, 31))
        self.d_DSB = QDoubleSpinBox(Form)
        self.d_DSB.setObjectName(u"doubleSpinBox")
        self.d_DSB.setGeometry(QRect(40, 140, 62, 24))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 111, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 100, 131, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 30, 251, 61))
        self.F_DSB = QDoubleSpinBox(Form)
        self.F_DSB.setObjectName(u"doubleSpinBox_2")
        self.F_DSB.setGeometry(QRect(160, 140, 62, 24))
        self.W_DSB = QDoubleSpinBox(Form)
        self.W_DSB.setObjectName(u"doubleSpinBox_3")
        self.W_DSB.setGeometry(QRect(310, 140, 62, 24))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 200, 111, 31))
        self.c_DSB = QDoubleSpinBox(Form)
        self.c_DSB.setObjectName(u"doubleSpinBox_4")
        self.c_DSB.setGeometry(QRect(150, 230, 62, 24))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 280, 80, 23))

        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(130, 280, 371, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Input for Work", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Input for Distance", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Input for Force", None))
        self.label.setText(QCoreApplication.translate("Form", u"Here you can calculate the Work Force", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Input for Grade", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
    # retranslateUi

