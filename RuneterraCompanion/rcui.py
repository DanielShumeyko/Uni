# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rcui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 379)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.VBox_main = QtWidgets.QVBoxLayout()
        self.VBox_main.setObjectName("VBox_main")
        self.VBox_decks = QtWidgets.QVBoxLayout()
        self.VBox_decks.setObjectName("VBox_decks")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.VBox_decks.addWidget(self.label_4)
        self.HBox_deckselect = QtWidgets.QHBoxLayout()
        self.HBox_deckselect.setObjectName("HBox_deckselect")
        self.combo_selectdeck = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_selectdeck.sizePolicy().hasHeightForWidth())
        self.combo_selectdeck.setSizePolicy(sizePolicy)
        self.combo_selectdeck.setObjectName("combo_selectdeck")
        self.combo_selectdeck.addItem("")
        self.HBox_deckselect.addWidget(self.combo_selectdeck)
        self.btn_deckadd = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_deckadd.sizePolicy().hasHeightForWidth())
        self.btn_deckadd.setSizePolicy(sizePolicy)
        self.btn_deckadd.setObjectName("btn_deckadd")
        self.HBox_deckselect.addWidget(self.btn_deckadd)
        self.btn_deckdel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_deckdel.sizePolicy().hasHeightForWidth())
        self.btn_deckdel.setSizePolicy(sizePolicy)
        self.btn_deckdel.setObjectName("btn_deckdel")
        self.HBox_deckselect.addWidget(self.btn_deckdel)
        self.HBox_deckselect.setStretch(0, 6)
        self.HBox_deckselect.setStretch(1, 2)
        self.HBox_deckselect.setStretch(2, 2)
        self.VBox_decks.addLayout(self.HBox_deckselect)
        self.VBox_main.addLayout(self.VBox_decks)
        self.HBox_input = QtWidgets.QHBoxLayout()
        self.HBox_input.setObjectName("HBox_input")
        self.VBox_winloss = QtWidgets.QVBoxLayout()
        self.VBox_winloss.setObjectName("VBox_winloss")
        self.label_winloss = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(28)
        self.label_winloss.setFont(font)
        self.label_winloss.setAlignment(QtCore.Qt.AlignCenter)
        self.label_winloss.setObjectName("label_winloss")
        self.VBox_winloss.addWidget(self.label_winloss)
        self.btn_win = QtWidgets.QPushButton(self.centralwidget)
        self.btn_win.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_win.sizePolicy().hasHeightForWidth())
        self.btn_win.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        self.btn_win.setFont(font)
        self.btn_win.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_win.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_win.setObjectName("btn_win")
        self.VBox_winloss.addWidget(self.btn_win)
        self.btn_loss = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_loss.sizePolicy().hasHeightForWidth())
        self.btn_loss.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        self.btn_loss.setFont(font)
        self.btn_loss.setObjectName("btn_loss")
        self.VBox_winloss.addWidget(self.btn_loss)
        self.VBox_winloss.setStretch(0, 5)
        self.VBox_winloss.setStretch(1, 2)
        self.VBox_winloss.setStretch(2, 2)
        self.HBox_input.addLayout(self.VBox_winloss)
        self.VBox_regions = QtWidgets.QVBoxLayout()
        self.VBox_regions.setObjectName("VBox_regions")
        self.label_regions = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(28)
        self.label_regions.setFont(font)
        self.label_regions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_regions.setObjectName("label_regions")
        self.VBox_regions.addWidget(self.label_regions)
        self.combo_region1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_region1.sizePolicy().hasHeightForWidth())
        self.combo_region1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        self.combo_region1.setFont(font)
        self.combo_region1.setObjectName("combo_region1")
        self.combo_region1.addItem("")
        self.combo_region1.addItem("")
        self.combo_region1.addItem("")
        self.combo_region1.addItem("")
        self.combo_region1.addItem("")
        self.combo_region1.addItem("")
        self.VBox_regions.addWidget(self.combo_region1)
        self.combo_region2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_region2.sizePolicy().hasHeightForWidth())
        self.combo_region2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.combo_region2.setFont(font)
        self.combo_region2.setObjectName("combo_region2")
        self.combo_region2.addItem("")
        self.combo_region2.addItem("")
        self.combo_region2.addItem("")
        self.combo_region2.addItem("")
        self.combo_region2.addItem("")
        self.combo_region2.addItem("")
        self.VBox_regions.addWidget(self.combo_region2)
        self.VBox_regions.setStretch(0, 5)
        self.VBox_regions.setStretch(1, 2)
        self.VBox_regions.setStretch(2, 2)
        self.HBox_input.addLayout(self.VBox_regions)
        self.VBox_champs = QtWidgets.QVBoxLayout()
        self.VBox_champs.setObjectName("VBox_champs")
        self.label_champs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(28)
        self.label_champs.setFont(font)
        self.label_champs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_champs.setObjectName("label_champs")
        self.VBox_champs.addWidget(self.label_champs)
        self.list_champs = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_champs.sizePolicy().hasHeightForWidth())
        self.list_champs.setSizePolicy(sizePolicy)
        self.list_champs.setObjectName("list_champs")
        item = QtWidgets.QListWidgetItem()
        self.list_champs.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_champs.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_champs.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_champs.addItem(item)
        self.VBox_champs.addWidget(self.list_champs)
        self.HBox_addchamps = QtWidgets.QHBoxLayout()
        self.HBox_addchamps.setObjectName("HBox_addchamps")
        self.btn_addchamp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addchamp.sizePolicy().hasHeightForWidth())
        self.btn_addchamp.setSizePolicy(sizePolicy)
        self.btn_addchamp.setObjectName("btn_addchamp")
        self.HBox_addchamps.addWidget(self.btn_addchamp)
        self.btn_delchamp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delchamp.sizePolicy().hasHeightForWidth())
        self.btn_delchamp.setSizePolicy(sizePolicy)
        self.btn_delchamp.setObjectName("btn_delchamp")
        self.HBox_addchamps.addWidget(self.btn_delchamp)
        self.VBox_champs.addLayout(self.HBox_addchamps)
        self.VBox_champs.setStretch(0, 1)
        self.VBox_champs.setStretch(1, 8)
        self.VBox_champs.setStretch(2, 1)
        self.HBox_input.addLayout(self.VBox_champs)
        self.HBox_input.setStretch(0, 2)
        self.HBox_input.setStretch(1, 2)
        self.HBox_input.setStretch(2, 5)
        self.VBox_main.addLayout(self.HBox_input)
        self.verticalLayout.addLayout(self.VBox_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Select Deck"))
        self.combo_selectdeck.setItemText(0, _translate("MainWindow", " Fiora \\ Shen OTK"))
        self.btn_deckadd.setText(_translate("MainWindow", "Add"))
        self.btn_deckdel.setText(_translate("MainWindow", "Delete"))
        self.label_winloss.setText(_translate("MainWindow", "VICTORY"))
        self.btn_win.setText(_translate("MainWindow", "Victory"))
        self.btn_loss.setText(_translate("MainWindow", "Defeat"))
        self.label_regions.setText(_translate("MainWindow", "REGIONS"))
        self.combo_region1.setItemText(0, _translate("MainWindow", "Shadow Isles"))
        self.combo_region1.setItemText(1, _translate("MainWindow", "Demacia"))
        self.combo_region1.setItemText(2, _translate("MainWindow", "Noxus"))
        self.combo_region1.setItemText(3, _translate("MainWindow", "Piltover & Zaun"))
        self.combo_region1.setItemText(4, _translate("MainWindow", "Ionia"))
        self.combo_region1.setItemText(5, _translate("MainWindow", "Freljord"))
        self.combo_region2.setItemText(0, _translate("MainWindow", "Freljord"))
        self.combo_region2.setItemText(1, _translate("MainWindow", "Shadow Isles"))
        self.combo_region2.setItemText(2, _translate("MainWindow", "Demacia"))
        self.combo_region2.setItemText(3, _translate("MainWindow", "Noxus"))
        self.combo_region2.setItemText(4, _translate("MainWindow", "Piltover & Zaun"))
        self.combo_region2.setItemText(5, _translate("MainWindow", "Ionia"))
        self.label_champs.setText(_translate("MainWindow", "CHAMPS"))
        __sortingEnabled = self.list_champs.isSortingEnabled()
        self.list_champs.setSortingEnabled(False)
        item = self.list_champs.item(0)
        item.setText(_translate("MainWindow", "Braum"))
        item = self.list_champs.item(1)
        item.setText(_translate("MainWindow", "Tryndamere"))
        item = self.list_champs.item(2)
        item.setText(_translate("MainWindow", "Thresh"))
        item = self.list_champs.item(3)
        item.setText(_translate("MainWindow", "Kalista"))
        self.list_champs.setSortingEnabled(__sortingEnabled)
        self.btn_addchamp.setText(_translate("MainWindow", "Add"))
        self.btn_delchamp.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

