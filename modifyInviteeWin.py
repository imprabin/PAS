import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLineEdit
from invitee import Invitee
import inviteeRepository
import organisationRepository
from organisation import Organisation

class Ui_ModifyInviteeDialog(QMainWindow):

    selected_id = 0

    def setupUi(self, ModifyInviteeDialog):
        ModifyInviteeDialog.setObjectName("ModifyInviteeDialog")
        ModifyInviteeDialog.setWindowIcon(QtGui.QIcon("PythonLogo.png"))
        ModifyInviteeDialog.setWindowModality(QtCore.Qt.WindowModal)
        ModifyInviteeDialog.resize(400, 227)
        ModifyInviteeDialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMod = QtWidgets.QPushButton(ModifyInviteeDialog)
        self.btnMod.setGeometry(QtCore.QRect(200, 190, 75, 23))
        self.btnMod.setObjectName("btnMod")
        self.gridLayoutWidget = QtWidgets.QWidget(ModifyInviteeDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 9, 391, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Namelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Namelabel.setObjectName("Namelabel")
        self.gridLayout.addWidget(self.Namelabel, 0, 0, 1, 1)
        self.NameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.NameLine.setObjectName("NameLine")
        self.gridLayout.addWidget(self.NameLine, 0, 1, 1, 1)
        self.Contactlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Contactlabel.setObjectName("Contactlabel")
        self.gridLayout.addWidget(self.Contactlabel, 1, 0, 1, 1)
        self.ContactLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ContactLine.setObjectName("ContactLine")
        self.gridLayout.addWidget(self.ContactLine, 1, 1, 1, 1)
        self.Orglabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Orglabel.setObjectName("Orglabel")
        self.gridLayout.addWidget(self.Orglabel, 2, 0, 1, 1)
        self.cmbOrg = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cmbOrg.setObjectName("cmbOrg")
        self.gridLayout.addWidget(self.cmbOrg, 2, 1, 1, 1)
        self.populateOrg()
        self.attendlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attendlabel.setObjectName("attendlabel")
        self.gridLayout.addWidget(self.attendlabel, 3, 0, 1, 1)
        self.attendChkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.attendChkBox.setChecked(False)
        self.attendChkBox.setObjectName("attendChkBox")
        self.gridLayout.addWidget(self.attendChkBox, 3, 1, 1, 1)
        self.noticeLabel = QtWidgets.QLabel(ModifyInviteeDialog)
        self.noticeLabel.setGeometry(QtCore.QRect(30, 180, 171, 16))
        self.noticeLabel.setObjectName("noticeLabel")
        self.populateRecord()
        self.btnMod.clicked.connect(self.onclickMod)
        self.retranslateUi(ModifyInviteeDialog)
        QtCore.QMetaObject.connectSlotsByName(ModifyInviteeDialog)


    def onclickMod(self):
        i_id = self.selected_id
        i_name = self.NameLine.text()
        if len(i_name) == 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Name Cannot be empty",
                                                   QMessageBox.Ok, QMessageBox.Ok)
            self.NameLine.setFocus()
            return
        i_org = self.cmbOrg.currentData()
        try:
           i_contact = int(self.ContactLine.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Contact Number must be numbers",
                                                       QMessageBox.Ok, QMessageBox.Ok)
            self.ContactLine.setFocus()
            self.ContactLine.selectAll()
            return
        emp = Invitee(self.selected_id, i_name, i_org, i_contact)
        if self.attendChkBox.isChecked():
            emp.attend = 1
        inviteeRepo = inviteeRepository.InviteeRepository
        inviteeRepo.modify(emp)



    def populateOrg(self):
        org = organisationRepository.OrganisationRepository()
        orgList = org.findAll()
        for org in orgList:
            self.cmbOrg.addItem(org.name, org.code)


    def retranslateUi(self, ModifyInviteeDialog):
        _translate = QtCore.QCoreApplication.translate
        ModifyInviteeDialog.setWindowTitle(_translate("ModifyInviteeDialog", "Modify"))
        self.btnMod.setText(_translate("AddInviteeDialog", "Modify"))
        self.Namelabel.setText(_translate("ModifyInviteeDialog", "Full Name"))
        self.Contactlabel.setText(_translate("ModifyInviteeDialog", "Contact No."))
        self.Orglabel.setText(_translate("ModifyInviteeDialog", "Organisation"))
        self.noticeLabel.setText(_translate("ModifyInviteeDialog", "*All Data must be entered"))
        self.attendlabel.setText(_translate("ModifyInviteeDialog", "Attendance"))

    def populateRecord(self):
        invRepo = inviteeRepository.InviteeRepository
        inv = invRepo.fetch(self.selected_id)
        self.NameLine.setText(inv.name)
        self.ContactLine.setText(str(inv.contactNo))
        for i in range(self.cmbOrg.count()):
            if self.cmbOrg.itemData(i) == inv.organisation:
                self.cmbOrg.setCurrentIndex(i)
                break
        if inv.attend == 1:
            self.attendChkBox.setChecked(True)