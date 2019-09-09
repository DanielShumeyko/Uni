from sys import exit as sysExit
from PyQt5.QtCore import Qt
from PyQt5.QtGui  import QFont, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QDockWidget, QStyleFactory, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMenuBar, QStatusBar
import PyQt5.QtWidgets as qtw

from model import LinearModel

class MenuToolBar(QDockWidget):
    def __init__(self, MainWin):
        QDockWidget.__init__(self)
        self.MainWin = MainWin
        self.MainMenu = MainWin.menuBar()

        # ******* Create the Help Menu *******
        self.HelpMenu  = self.MainMenu.addMenu('Help')

class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)

    # General Font Object for a couple of Buttons
        btnFont = QFont()
        btnFont.setFamily('Arial')
        btnFont.setItalic(True)
    # Horizontal Box 1 containing instruction label.
        self.instruction = QLabel(self)
        self.instruction.setFont(QFont("Times", 8, QFont.Bold))
        self.instruction.setText('Please set the parameters below. If you have trouble click the \'Help\' tab above.')     


        HBox1 = QHBoxLayout()
        HBox1.addWidget(self.instruction)

    # Vertical layouts for parameter input

        self.label_a1 = QLabel(self)
        self.label_a1.setText('                    a1')
        self.label_a1.setFont(QFont("Times", 8, QFont.Bold))
        self.input_a1 = QLineEdit(self)
        VBox1 = QVBoxLayout()
        VBox1.addWidget(self.label_a1)
        VBox1.addWidget(self.input_a1)

        self.label_a2 = QLabel(self)
        self.label_a2.setText('                    a2')
        self.label_a2.setFont(QFont("Times", 8, QFont.Bold))
        self.input_a2 = QLineEdit(self)
        VBox2 = QVBoxLayout()
        VBox2.addWidget(self.label_a2)
        VBox2.addWidget(self.input_a2)

        self.label_b = QLabel(self)
        self.label_b.setText('                    b')
        self.label_b.setFont(QFont("Times", 8, QFont.Bold))
        self.input_b = QLineEdit(self)
        VBox3 = QVBoxLayout()
        VBox3.addWidget(self.label_b)
        VBox3.addWidget(self.input_b)

        self.label_q = QLabel(self)
        self.label_q.setText('                    q')
        self.label_q.setFont(QFont("Times", 8, QFont.Bold))
        self.input_q = QLineEdit(self)
        VBox4 = QVBoxLayout()
        VBox4.addWidget(self.label_q)
        VBox4.addWidget(self.input_q)

        self.label_t = QLabel(self)
        self.label_t.setText('                    To')
        self.label_t.setFont(QFont("Times", 8, QFont.Bold))
        self.input_t = QLineEdit(self)
        VBox5 = QVBoxLayout()
        VBox5.addWidget(self.label_t)
        VBox5.addWidget(self.input_t)

    # Horizontal Layout 2 for all the inputs
        HBox2 = QHBoxLayout()
        HBox2.addLayout(VBox1)
        HBox2.addLayout(VBox2)
        HBox2.addLayout(VBox3)
        HBox2.addLayout(VBox4)
        HBox2.addLayout(VBox5)

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

        self.setWindowTitle('Lab 1 / Processes in Linear Systems')
        self.resize(500, 150)
        self.CenterPane = CenterPanel(self)

        self.setCentralWidget(self.CenterPane)
        self.MenuBar = MenuToolBar(self)

        self.SetStatusBar(self)
        self.setStyle(QStyleFactory.create('Cleanlooks'))

    def SetStatusBar(self, parent):
        StatusMsg = ''
        parent.StatBar = parent.statusBar()

        if len(StatusMsg) < 1:
            StatusMsg = 'Ready'

        parent.StatBar.showMessage(StatusMsg)

    def inputParams(self):
        a1 = int(self.CenterPane.input_a1.text())
        a2 = int(self.CenterPane.input_a2.text())
        b = int(self.CenterPane.input_b.text())
        q = int(self.CenterPane.input_q.text())
        t = float(self.CenterPane.input_t.text())

        self.CenterPane.input_a1.clear()
        self.CenterPane.input_a2.clear()
        self.CenterPane.input_b.clear()
        self.CenterPane.input_q.clear()
        self.CenterPane.input_t.clear()

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
            self.LoadModel(a1, a2, b, q, t)

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
    
    def LoadModel(self, a1, a2, b, q, t):
        mdl = LinearModel(a1, a2, b, q, t)
        mdl.runModel()
        
if __name__ == "__main__":
    MainThread = QApplication([])
    MainGUI = MainWindow()
    MainGUI.show()
    sysExit(MainThread.exec_())