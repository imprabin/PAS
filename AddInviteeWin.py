
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon
from invitee import Invitee
import inviteeRepository
import organisationRepository
from organisation import Organisation

class Ui_AddInviteeDialog(QMainWindow):

    selected_id = 0

    def setupUi3(self, AddInviteeDialog):
        AddInviteeDialog.setObjectName("AddInviteeDialog")
        AddInviteeDialog.setWindowIcon(QIcon("PythonLogo.png"))
        AddInviteeDialog.setWindowModality(QtCore.Qt.WindowModal)
        AddInviteeDialog.resize(400, 227)
        AddInviteeDialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnAdd = QtWidgets.QPushButton(AddInviteeDialog)
        self.btnAdd.setGeometry(QtCore.QRect(310, 190, 75, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayoutWidget = QtWidgets.QWidget(AddInviteeDialog)
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

        self.cmbOrg = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cmbOrg.setObjectName("cmbOrg")
        self.gridLayout.addWidget(self.cmbOrg, 2, 1, 1, 1)
        self.populateOrg()
        self.Contactlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Contactlabel.setObjectName("Contactlabel")
        self.gridLayout.addWidget(self.Contactlabel, 1, 0, 1, 1)
        self.Orglabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Orglabel.setObjectName("Orglabel")
        self.gridLayout.addWidget(self.Orglabel, 2, 0, 1, 1)
        self.ContactLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ContactLine.setObjectName("ContactLine")
        self.gridLayout.addWidget(self.ContactLine, 1, 1, 1, 1)
        self.noticeLabel = QtWidgets.QLabel(AddInviteeDialog)
        self.noticeLabel.setGeometry(QtCore.QRect(30, 180, 171, 16))
        # self.noticeLabel.setObjectName("noticeLabel")
        self.btnAdd.clicked.connect(self.onclickAdd)
        self.btnAdd.clicked.connect(AddInviteeDialog.close)
        self.retranslateUi(AddInviteeDialog)
        QtCore.QMetaObject.connectSlotsByName(AddInviteeDialog)

    def onclickAdd(self):
        i_name = self.NameLine.text()
        if len(i_name) == 0:
            choice = QtWidgets.QMessageBox.warning(self, "Error", "Name Cannot be empty",
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
        emp = Invitee(None, i_name, i_org, i_contact)
        inviteeRepo = inviteeRepository.InviteeRepository
        inviteeRepo.add(emp)
        self.hide()

    def populateOrg(self):
        orgList = organisationRepository.OrganisationRepository.findAll(self)
        for org in orgList:
            self.cmbOrg.addItem(org.name, org.code)


    def retranslateUi(self, AddInviteeDialog):
        _translate = QtCore.QCoreApplication.translate
        AddInviteeDialog.setWindowTitle(_translate("AddInviteeDialog", "Add Invitee"))
        self.btnAdd.setText(_translate("AddInviteeDialog", "Add"))
        self.Namelabel.setText(_translate("AddInviteeDialog", "Full Name"))
        self.Contactlabel.setText(_translate("AddInviteeDialog", "Contact No."))
        self.Orglabel.setText(_translate("AddInviteeDialog", "Organisation"))
        self.noticeLabel.setText(_translate("AddInviteeDialog", "*All Data must be entered"))

    def populateRecord(self):
        if self.selected_id is None:
            return
        invRepo = inviteeRepository.InviteeRepository
        inv = invRepo.fetch(self.selected_id)
        self.NameLine.setText(inv.name)
        self.ContactLine.setText(str(inv.contactNo))
        for i in range(self.cmbOrg.count()):
            if self.cmbOrg.itemData(i) == inv.organisation:
                self.cmbOrg.setCurrentIndex(i)
                break