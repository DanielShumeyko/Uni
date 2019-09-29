from sys import exit as sysExit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout



class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)

    # Sub layouts (These get sandwitched into the main layout)


    # Other elements of main layout


    # Main Layout
        VBoxM = QVBoxLayout()
        self.setLayout(VBoxM)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Window Title')
        self.resize(500, 500)
        self.CenterPane = CenterPanel(self)
        self.setCentralWidget(self.CenterPane)


        
if __name__ == "__main__":
    MainThread = QApplication([])
    MainGUI = MainWindow()
    MainGUI.show()
    sysExit(MainThread.exec_())