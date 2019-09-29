from sys import exit as sysExit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QDockWidget, QStyleFactory, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel

nle = 'x^3 + sin(x) - 12x + 1 = 0'
epsilon = 0.001

class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)

    # Sub layouts (These get sandwitched into the main layout)

        # VBox1 sublayout containing labels for introduction, displaying the equation, displaying epsilon and asking the user to choose a method 
        self.label_intro = QLabel(self)
        self.label_intro.setFont(QFont("Times", 14, QFont.Bold))
        self.label_intro.setText('Modified Newton\'s and Dichotomy methods for solving nonlinear equations')
        self.label_intro.setAlignment(Qt.AlignCenter)

        self.label_equation = QLabel(self)
        self.label_equation.setFont(QFont("Times", 12, QFont.AnyStyle))
        self.label_equation.setText('The equation we will be solving is ' + nle)
        self.label_equation.setAlignment(Qt.AlignCenter)

        self.label_eps = QLabel(self)
        self.label_eps.setFont(QFont("Times", 12, QFont.AnyStyle))
        self.label_eps.setText('Epsilon (precision with which we calculate the answer) is ' + str(epsilon))
        self.label_eps.setAlignment(Qt.AlignCenter)

        VBox1 = QVBoxLayout()
        VBox1.addWidget(self.label_intro)
        VBox1.addWidget(self.label_equation)
        VBox1.addWidget(self.label_eps)


        
        # HBox1 sublayout containing buttons for Newton's Modified and Dichotomy methods
        self.btn_method1 = QPushButton()
        self.btn_method1.setFont(QFont("Times", 12, QFont.Bold))
        self.btn_method1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_method1.setText('Modified Newton\'s')

        self.btn_method2 = QPushButton()
        self.btn_method2.setFont(QFont("Times", 12, QFont.Bold))
        self.btn_method2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_method2.setText('Dichotomy')

        HBox1 = QHBoxLayout()
        HBox1.addWidget(self.btn_method1)
        HBox1.addWidget(self.btn_method2)


    # Other elements of main layout


    # Main Layout
        VBoxM = QVBoxLayout()
        VBoxM.addLayout(VBox1)
        VBoxM.addLayout(HBox1)
        
        self.setLayout(VBoxM)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Lab 1 / Nonlinear equation ')
        self.resize(500, 150)
        self.CenterPane = CenterPanel(self)
        self.setCentralWidget(self.CenterPane)


        
if __name__ == "__main__":
    MainThread = QApplication([])
    MainGUI = MainWindow()
    MainGUI.show()
    sysExit(MainThread.exec_())