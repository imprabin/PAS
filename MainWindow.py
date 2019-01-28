# import sys
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from AddInviteeWin import Ui_AddInviteeDialog
from viewAll import Ui_viewAll
from modifyInviteeWin import Ui_ModifyInviteeDialog
from ManageOrg import Ui_MainOrgWindow

class Ui_MainWindow(QMainWindow):

    def AddInvitee(self):
        self.AddInviteeDialog = QtWidgets.QDialog()
        self.ui = Ui_AddInviteeDialog()
        self.ui.setupUi3(self.AddInviteeDialog)
        self.AddInviteeDialog.show()

    def viewInvitee(self):
        self.viewAll = QtWidgets.QMainWindow()
        self.ui = Ui_viewAll()
        self.ui.setupUi(self.viewAll)
        self.viewAll.show()
        self.hide()

    def manageOrgClicked(self):
        self.MainOrgWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainOrgWindow()
        self.ui.setupUi(self.MainOrgWindow)
        self.MainOrgWindow.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("PythonLogo.png"))
        MainWindow.resize(380, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 317, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnView = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnView.setObjectName("btnView")
        self.gridLayout.addWidget(self.btnView, 2, 1, 1, 1)
        self.btnAddInvitee = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAddInvitee.setObjectName("btnAddInvitee")
        self.gridLayout.addWidget(self.btnAddInvitee, 2, 0, 1, 1)
        self.btnAttendance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAttendance.setObjectName("btnAttendance")
        self.gridLayout.addWidget(self.btnAttendance, 3, 0, 1, 1)
        self.btnOrganisation = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnOrganisation.setObjectName("btnOrganisation")
        self.gridLayout.addWidget(self.btnOrganisation, 3, 1, 1, 1)
        self.headingLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.headingLabel.setFont(font)
        self.headingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headingLabel.setObjectName("headingLabel")
        self.gridLayout.addWidget(self.headingLabel, 0, 0, 2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.actionView = QtWidgets.QAction(MainWindow)
        self.actionView.setObjectName("actionView")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionView)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##########File Menu and button  action#########################
        self.actionExit.triggered.connect(self.exit)
        self.actionView.triggered.connect(self.viewInvitee)
        self.btnAddInvitee.clicked.connect(self.AddInvitee)
        self.btnView.clicked.connect(self.viewInvitee)
        self.btnAttendance.clicked.connect(self.viewInvitee)
        self.btnOrganisation.clicked.connect(self.manageOrgClicked)
        ################################################

    def exit(self):
        choice = QtWidgets.QMessageBox.question(self, "Exit", "Do you want to quit?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
           sys.exit()
        else:
           pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnView.setText(_translate("MainWindow", "View"))
        self.btnOrganisation.setText(_translate("MainWindow", "Manage Organisation"))
        self.btnAddInvitee.setText(_translate("MainWindow", "Add Invitee"))
        self.btnAttendance.setText(_translate("MainWindow", "Attendance"))
        self.headingLabel.setText(_translate("MainWindow", "Program Attendance System"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionView.setText(_translate("MainWindow", "View Invitees"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
