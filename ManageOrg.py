# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageOrg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox,QLabel
import organisationRepository
import organisation


class Ui_MainOrgWindow(QMainWindow):

    selected_code = ''

    def setupUi(self, MainOrgWindow):
        MainOrgWindow.setObjectName("MainOrgWindow")
        MainOrgWindow.resize(607, 282)
        self.centralwidget = QtWidgets.QWidget(MainOrgWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.orgTable = QtWidgets.QTableWidget(self.centralwidget)
        self.orgTable.setGeometry(QtCore.QRect(250, 10, 341, 231))
        self.orgTable.setRowCount(20)
        self.orgTable.setColumnCount(3)
        self.orgTable.setObjectName("orgTable")
        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setGeometry(QtCore.QRect(500, 250, 75, 23))
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnModOrg = QtWidgets.QPushButton(self.centralwidget)
        self.btnModOrg.setGeometry(QtCore.QRect(400, 250, 75, 23))
        self.btnModOrg.setObjectName("btnModOrg")

        self.btnAddOrg = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddOrg.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.btnAddOrg.setObjectName("btnAddOrg")

        self.btnModifyOrg = QtWidgets.QPushButton(self.centralwidget)
        self.btnModifyOrg.setGeometry(QtCore.QRect(150, 250, 75, 23))
        self.btnModifyOrg.setObjectName("btnModifyOrg")

        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(300, 250, 75, 23))
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 20, 231, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.orgCodeLbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.orgCodeLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.orgCodeLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.orgCodeLbl.setObjectName("orgCodeLbl")
        self.gridLayout.addWidget(self.orgCodeLbl, 0, 0, 1, 1)
        self.orgNameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.orgNameLine.setObjectName("orgNameLine")
        self.gridLayout.addWidget(self.orgNameLine, 1, 1, 1, 1)
        self.orgNameLbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.orgNameLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.orgNameLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.orgNameLbl.setObjectName("orgNameLbl")
        self.gridLayout.addWidget(self.orgNameLbl, 1, 0, 1, 1)
        self.orgCodeLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.orgCodeLine.setObjectName("orgCodeLine")
        self.gridLayout.addWidget(self.orgCodeLine, 0, 1, 1, 1)
        self.addressOrgLbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.addressOrgLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.addressOrgLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.addressOrgLbl.setObjectName("addressOrgLbl")
        self.gridLayout.addWidget(self.addressOrgLbl, 2, 0, 1, 1)
        self.orgAddLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.orgAddLine.setObjectName("orgAddLine")
        self.gridLayout.addWidget(self.orgAddLine, 2, 1, 1, 1)

        self.noticeLabel = QtWidgets.QLabel(MainOrgWindow)
        self.noticeLabel.setGeometry(QtCore.QRect(70, 60, 171, 16))
        self.noticeLabel.setObjectName("noticeLabel")

        item = QtWidgets.QTableWidgetItem()
        self.orgTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orgTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orgTable.setHorizontalHeaderItem(2, item)

        MainOrgWindow.setCentralWidget(self.centralwidget)
        self.loadTable()

        self.btnRefresh.clicked.connect(self.loadTable)
        self.btnModOrg.clicked.connect(self.loadOrgData)
        self.orgTable.clicked.connect(self.tableClicked)
        self.btnAddOrg.clicked.connect(self.addOrg)
        self.btnDelete.clicked.connect(self.deleteOrgclick)
        self.retranslateUi(MainOrgWindow)
        QtCore.QMetaObject.connectSlotsByName(MainOrgWindow)

    def retranslateUi(self, MainOrgWindow):
        _translate = QtCore.QCoreApplication.translate
        MainOrgWindow.setWindowTitle(_translate("MainOrgWindow", "Organisations"))
        self.btnRefresh.setText(_translate("MainOrgWindow", "Refresh"))
        self.btnModOrg.setText(_translate("MainOrgWindow", "Edit Org"))
        self.btnAddOrg.setText(_translate("MainOrgWindow", "Add Org"))
        self.btnModifyOrg.setText(_translate("MainOrgWindow", "Modify Org"))
        self.btnDelete.setText(_translate("MainOrgWindow", "Delete"))
        self.orgCodeLbl.setText(_translate("MainOrgWindow", "Code"))
        self.orgNameLbl.setText(_translate("MainOrgWindow", "Organisation"))
        self.addressOrgLbl.setText(_translate("MainOrgWindow", "Address"))
        self.noticeLabel.setText(_translate("MainOrgWindow", "Please use format ''C0xx'' for code"))

        item = self.orgTable.horizontalHeaderItem(0)
        item.setText(_translate("orgTable", "Code"))
        item = self.orgTable.horizontalHeaderItem(1)
        item.setText(_translate("orgTable", "Org Name"))
        item = self.orgTable.horizontalHeaderItem(2)
        item.setText(_translate("orgTable", "Address"))

    def loadTable(self):
        org =organisationRepository.OrganisationRepository
        org.loadOrgTable(self)

    def tableClicked(self, signal):
        row = signal.row()
        column = signal.column()
        self.orgTable.selectRow(row)
        self.selected_code = self.orgTable.item(row,0).text()

    def loadOrgData(self):
        orgRepo = organisationRepository.OrganisationRepository
        org = orgRepo.fetchOrg(self.selected_code)
        self.orgCodeLine.setText(org.code)
        self.orgNameLine.setText(org.name)
        self.orgAddLine.setText(org.address)
        self.btnModifyOrg.clicked.connect(self.modifyOrg)

    def modifyOrg(self):
        orgRepo = organisationRepository.OrganisationRepository
        n_code = self.orgCodeLine.text()
        print(n_code)
        try:
            if self.compareUnique(n_code):
                QtWidgets.QMessageBox.warning(self, "Error", "Organisation Code does not exist to modify!", QMessageBox.Ok,
                                              QMessageBox.Ok)
                print("Organisation code doesnot exists")
        except Exception as err:
            print("Error compare", err)
        n_name = self.orgNameLine.text()
        n_add = self.orgAddLine.text()
        organise = organisation.Organisation(n_code, n_name, n_add)
        orgRepo.modOrg(organise)
        self.loadTable()

    def addOrg(self):
        orgRepo = organisationRepository.OrganisationRepository
        o_code = self.orgCodeLine.text()
        if o_code == "":
            QMessageBox.warning(self, "Error", "Organisation Code cannot be blank!", QMessageBox.Ok,
                                          QMessageBox.Ok)


            return


        if not self.compareUnique(o_code):
            QtWidgets.QMessageBox.warning(self, "Error", "Organisation Code is not unique!", QMessageBox.Ok,
                                          QMessageBox.Ok)
            return

        o_name = self.orgNameLine.text()
        o_address = self.orgAddLine.text()
        org = organisation.Organisation(o_code, o_name, o_address)
        orgRepo.add_org(org)
        self.loadTable()

    def compareUnique(self, c):
        orgRepo = organisationRepository.OrganisationRepository
        if orgRepo.unique(c):
            return True
        return False

    def deleteOrgclick(self):
        orgRepo = organisationRepository.OrganisationRepository
        orgRepo.deleteOrg(self.selected_code)
        self.loadTable()




# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainOrgWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainOrgWindow()
#     ui.setupUi(MainOrgWindow)
#     MainOrgWindow.show()
#     sys.exit(app.exec())
