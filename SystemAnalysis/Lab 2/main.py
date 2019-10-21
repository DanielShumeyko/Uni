# Daniel Shumeyko, PS-3

from sys import exit as sysExit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QDockWidget, QStyleFactory, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
from model import DynamicModel


class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)

    # Horizontal Box 1 containing instruction label.
        self.instruction = QLabel(self)
        self.instruction.setFont(QFont("Times", 8, QFont.Bold))
        self.instruction.setText('Please set the parameters below.')     


        HBox1 = QHBoxLayout()
        HBox1.addWidget(self.instruction)

    # Vertical layouts for parameter input

        self.label_a1 = QLabel(self)
        self.label_a1.setText('                a1')
        self.label_a1.setFont(QFont("Times", 10, QFont.Bold))
        self.input_a1 = QLineEdit(self)
        VBox1 = QVBoxLayout()
        VBox1.addWidget(self.label_a1)
        VBox1.addWidget(self.input_a1)

        self.label_a2 = QLabel(self)
        self.label_a2.setText('                a2')
        self.label_a2.setFont(QFont("Times", 10, QFont.Bold))
        self.input_a2 = QLineEdit(self)
        VBox2 = QVBoxLayout()
        VBox2.addWidget(self.label_a2)
        VBox2.addWidget(self.input_a2)

        self.label_b = QLabel(self)
        self.label_b.setText('                b')
        self.label_b.setFont(QFont("Times", 10, QFont.Bold))
        self.input_b = QLineEdit(self)
        VBox3 = QVBoxLayout()
        VBox3.addWidget(self.label_b)
        VBox3.addWidget(self.input_b)

        self.label_q = QLabel(self)
        self.label_q.setText('                q')
        self.label_q.setFont(QFont("Times", 10, QFont.Bold))
        self.input_q = QLineEdit(self)
        VBox4 = QVBoxLayout()
        VBox4.addWidget(self.label_q)
        VBox4.addWidget(self.input_q)

        self.label_t = QLabel(self)
        self.label_t.setText('                To')
        self.label_t.setFont(QFont("Times", 10, QFont.Bold))
        self.input_t = QLineEdit(self)
        VBox5 = QVBoxLayout()
        VBox5.addWidget(self.label_t)
        VBox5.addWidget(self.input_t)

        self.label_ko = QLabel(self)
        self.label_ko.setText('                ko')
        self.label_ko.setFont(QFont("Times", 10, QFont.Bold))
        self.input_ko = QLineEdit(self)
        VBox6 = QVBoxLayout()
        VBox6.addWidget(self.label_ko)
        VBox6.addWidget(self.input_ko)

        self.label_xo = QLabel(self)
        self.label_xo.setText('                Xo')
        self.label_xo.setFont(QFont("Times", 10, QFont.Bold))
        self.input_xo = QLineEdit(self)
        VBox7 = QVBoxLayout()
        VBox7.addWidget(self.label_xo)
        VBox7.addWidget(self.input_xo)

        self.label_l2 = QLabel(self)
        self.label_l2.setText('          delta l2')
        self.label_l2.setFont(QFont("Times", 10, QFont.Bold))
        self.input_l2 = QLineEdit(self)
        VBox8 = QVBoxLayout()
        VBox8.addWidget(self.label_l2)
        VBox8.addWidget(self.input_l2)

        self.label_l3 = QLabel(self)
        self.label_l3.setText('          delta l3')
        self.label_l3.setFont(QFont("Times", 10, QFont.Bold))
        self.input_l3 = QLineEdit(self)
        VBox9 = QVBoxLayout()
        VBox9.addWidget(self.label_l3)
        VBox9.addWidget(self.input_l3)

    # Horizontal Layout 2 for all the inputs
        HBox2 = QHBoxLayout()
        HBox2.addLayout(VBox1)
        HBox2.addLayout(VBox2)
        HBox2.addLayout(VBox3)
        HBox2.addLayout(VBox4)
        HBox2.addLayout(VBox5)
        HBox2.addLayout(VBox6)
        HBox2.addLayout(VBox7)
        HBox2.addLayout(VBox8)
        HBox2.addLayout(VBox9)

    # Main Layout
        self.confirm = QPushButton()
        self.confirm.setFont(QFont("Times", 8, QFont.Bold))
        self.confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm.setText('Input Parameters')
        self.confirm.clicked.connect(parent.inputParams)


        VBoxM = QVBoxLayout()
        VBoxM.addLayout(HBox1)
        VBoxM.addLayout(HBox2)
        VBoxM.addWidget(self.confirm)

        self.setLayout(VBoxM)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Lab 2 / Dynamic Models')
        self.resize(500, 150)
        self.CenterPane = CenterPanel(self)

        self.setCentralWidget(self.CenterPane)
        self.setStyle(QStyleFactory.create('Cleanlooks'))

    def inputParams(self):
        a1 = int(self.CenterPane.input_a1.text())
        a2 = int(self.CenterPane.input_a2.text())
        b = int(self.CenterPane.input_b.text())
        q = int(self.CenterPane.input_q.text())
        t = float(self.CenterPane.input_t.text())
        ko = int(self.CenterPane.input_ko.text())
        xo = float(self.CenterPane.input_xo.text())
        l2 = float(self.CenterPane.input_l2.text())
        l3 = float(self.CenterPane.input_l3.text())

        self.CenterPane.input_a1.clear()
        self.CenterPane.input_a2.clear()
        self.CenterPane.input_b.clear()
        self.CenterPane.input_q.clear()
        self.CenterPane.input_t.clear()
        self.CenterPane.input_ko.clear()
        self.CenterPane.input_xo.clear()
        self.CenterPane.input_l2.clear()
        self.CenterPane.input_l3.clear()
        ABOUNDLOW = 1
        ABOUNDHIGH = 10
        QBOUNDLOW = 1
        QBOUNDHIGH = 10
        TBOUNDLOW = 0.001
        TBOUNDHIGH = 0.1

        if a1 > ABOUNDHIGH or a1 < ABOUNDLOW:
            self.msgOOB('a1')
        elif a2 > ABOUNDHIGH or a2 < ABOUNDLOW:
            self.msgOOB('a2')
        elif t > TBOUNDHIGH or t < TBOUNDLOW:
            self.msgOOB('t')
        elif q > QBOUNDHIGH or q < QBOUNDLOW:
            self.msgOOB('q')
        else:
            self.LoadModel(a1, a2, b, q, t, ko, xo, l2, l3)

    def msgOOB(self, error=''):

        if error == 'a1':
            text = 'Parameter a1 has to be between 1 and 10'
        elif error == 'a2':
            text = 'Parameter a2 has to be between 1 and 10'
        elif error == 't':
            text = 'Parameter To has to be between 0.001 and 0.1'
        elif error == 'q':
            text = 'Parameter q has to be between 1 and 10'
        else:
            text = 'unknown error'

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText(text)
        msg.setInformativeText("Please enter an acceptable value.")
        msg.setWindowTitle("Parameter out of range")
        msg.setDetailedText("Parameter ranges: \n a1 - [1;10] \n a2 - [1;10] \n To - [0.001; 0.1] \n q - [1;10]")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
        msg.exec_()
    
    def LoadModel(self, a1, a2, b, q, t, ko, xo, l2, l3):
        mdl = DynamicModel(a1, a2, b, q, t, ko, xo, l2, l3)
        mdl.printData()
        mdl.runModel()
        
if __name__ == "__main__":
    MainThread = QApplication([])
    MainGUI = MainWindow()
    MainGUI.show()
    sysExit(MainThread.exec_())

# Daniel Shumeyko, PS-3