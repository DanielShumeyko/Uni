import numpy as np
from sys import exit as sysExit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTextBrowser
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel

from linearsys import Square_Roots, Seidel

A = np.matrix([[3, 1, 1],[1, 7, 5],[3, 3, 6]])
b = np.array([1, 3, 2])
Eps = 0.001
x0 = [0, 0, 0]

class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)

    # Sub layouts (These get sandwitched into the main layout)

        # VBox1 sublayout containing labels for introduction, displaying the equation, displaying epsilon and asking the user to choose a method 
        self.label_intro = QLabel(self)
        self.label_intro.setFont(QFont("Times", 14, QFont.Bold))
        self.label_intro.setText('Square Roots and Seidel methods for solving systems of linear equations')
        self.label_intro.setAlignment(Qt.AlignCenter)

        self.label_equation = QLabel(self)
        self.label_equation.setFont(QFont("Times", 12, QFont.AnyStyle))
        self.label_equation.setText('Matrix A is \n' + str(A) + '\n Vector b is ' + str(b))
        self.label_equation.setAlignment(Qt.AlignCenter)

        self.label_eps = QLabel(self)
        self.label_eps.setFont(QFont("Times", 12, QFont.AnyStyle))
        self.label_eps.setText('Epsilon (precision) is ' + str(Eps))
        self.label_eps.setAlignment(Qt.AlignCenter)

        VBox1 = QVBoxLayout()
        VBox1.addWidget(self.label_intro)
        VBox1.addWidget(self.label_equation)
        VBox1.addWidget(self.label_eps)


        
        # HBox1 sublayout containing buttons for Newton's Modified and Dichotomy methods
        self.btn_method1 = QPushButton()
        self.btn_method1.setFont(QFont("Times", 12, QFont.Bold))
        self.btn_method1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_method1.setText('Square Roots')


        self.btn_method2 = QPushButton()
        self.btn_method2.setFont(QFont("Times", 12, QFont.Bold))
        self.btn_method2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_method2.setText('Seidel')
        self.btn_method2.clicked.connect(parent.runSeidel)


        HBox1 = QHBoxLayout()
        HBox1.addWidget(self.btn_method1)
        HBox1.addWidget(self.btn_method2)


    # Other elements of main layout
        self.outp_area = QTextBrowser()


    # Main Layout
        VBoxM = QVBoxLayout()
        VBoxM.addLayout(VBox1)
        VBoxM.addLayout(HBox1)
        VBoxM.addWidget(self.outp_area)
        
        self.setLayout(VBoxM)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Lab 1 / Nonlinear equation ')
        self.resize(500, 550)
        self.CenterPane = CenterPanel(self)
        self.setCentralWidget(self.CenterPane)

    def runSeidel(self):
        mdl = Seidel()
        log = mdl.run()
        self.CenterPane.outp_area.append(log)
        self.resize(500, 549)
        self.resize(500, 550)
        
if __name__ == "__main__":
    MainThread = QApplication([])
    MainGUI = MainWindow()
    MainGUI.show()
    sysExit(MainThread.exec_())