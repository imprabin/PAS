import sys
import sqlite3
import xlwt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from invitee import Invitee
import inviteeRepository
from modifyInviteeWin import Ui_ModifyInviteeDialog
from AddInviteeWin import *


class Ui_viewAll(QMainWindow):

    def __init__(self):
        super().__init__()

    selected_id = 0

    def attendWin(self):
        inviteeRepo = inviteeRepository.InviteeRepository
        inviteeRepo.doattend(self.selected_id)
        self.load_table()

    def delete_row(self):
        if not self.checkRowSelected():
            return
        choice = QtWidgets.QMessageBox.question(self, "Confirm", "Are you sure to delete?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.No:
            return
        inviteeRepo = inviteeRepository.InviteeRepository
        inviteeRepo.remove(self.selected_id)
        self.load_table()


    def load_table(self):
        inviteeRepo = inviteeRepository.InviteeRepository
        inviteeRepo.load_data(self)
        self.selected_id =0

    def modRow(self):
        if not self.checkRowSelected():
            return
        self.ModifyInviteeDialog = QtWidgets.QDialog()
        self.ui = Ui_ModifyInviteeDialog()
        self.ui.selected_id = self.selected_id
        self.ui.setupUi(self.ModifyInviteeDialog)
        self.ModifyInviteeDialog.show()

    def checkRowSelected(self):
        if self.selected_id == 0:
            QtWidgets.QMessageBox.warning(self, "Error", "No rows are selected",QMessageBox.Ok, QMessageBox.Ok)
            return False
        return True

    def saveFile(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
        print(filename)
        wbk = xlwt.Workbook()
        self.sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        self.add2()
        wbk.save(filename)

    def add2(self):
        row = 0
        col = 0
        for i in range(self.dataTable.columnCount()):
            for x in range(self.dataTable.rowCount()+1):
                try:
                    if row == 0:
                        teext = str(self.dataTable.horizontalHeaderItem(col).text())
                    else:
                        teext = str(self.dataTable.item(row-1, col).text())
                    self.sheet.write(row, col, teext)
                    row += 1
                except AttributeError:
                    row += 1
            row = 0
            col += 1



    def setupUi(self, viewAll):
        super().__init__()
        viewAll.setObjectName("viewAll")
        viewAll.setWindowIcon(QtGui.QIcon("PythonLogo.png"))
        viewAll.resize(510, 295)
        self.dataTable_2 = QtWidgets.QWidget(viewAll)
        self.dataTable_2.setObjectName("dataTable_2")
        self.btnRemoveRow = QtWidgets.QPushButton(self.dataTable_2)
        self.btnRemoveRow.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.btnRemoveRow.setObjectName("btnRemoveRow")
        self.btnModifyRow = QtWidgets.QPushButton(self.dataTable_2)
        self.btnModifyRow.setGeometry(QtCore.QRect(200, 260, 75, 23))
        self.btnModifyRow.setObjectName("btnModifyRow")
        self.btnExport= QtWidgets.QPushButton(self.dataTable_2)
        self.btnExport.setGeometry(QtCore.QRect(10, 2, 75, 21))
        self.btnExport.setObjectName("btnExport")

        self.btnAttend = QtWidgets.QPushButton(self.dataTable_2)
        self.btnAttend.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.btnAttend.setObjectName("btnAttend")

        self.dataTable = QtWidgets.QTableWidget(self.dataTable_2)
        self.dataTable.setGeometry(QtCore.QRect(8, 25, 496, 230))
        self.dataTable.setRowCount(50)
        self.dataTable.setColumnCount(5)
        self.dataTable.setObjectName("dataTable")

        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)

        self.btnViewAll = QtWidgets.QPushButton(self.dataTable_2)
        self.btnViewAll.setGeometry(QtCore.QRect(400, 260, 75, 23))
        self.btnViewAll.setObjectName("btnViewAll")
        viewAll.setCentralWidget(self.dataTable_2)

        self.btnViewAll.clicked.connect(self.load_table)

        self.dataTable.clicked.connect(self.Clicked_table)
        self.btnRemoveRow.clicked.connect(self.delete_row)
        self.btnModifyRow.clicked.connect(self.modRow)
        self.btnAttend.clicked.connect(self.attendWin)
        self.btnExport.clicked.connect(self.saveFile)

        self.retranslateUi(viewAll)
        QtCore.QMetaObject.connectSlotsByName(viewAll)

    def Clicked_table(self, signal):
        row = signal.row()
        column = signal.column()
        self.dataTable.selectRow(row)
        self.selected_id = int(self.dataTable.item(row, 0).text())

    def retranslateUi(self, viewAll):
        _translate = QtCore.QCoreApplication.translate
        viewAll.setWindowTitle(_translate("MainWindow", "Data View"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("viewAll", "ID"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("viewAll", "Name"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("viewAll", "Organisation"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("viewAll", "Contact No"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("viewAll", "Attendance"))
        self.btnRemoveRow.setText(_translate("viewAll", "Delete Row"))
        self.btnModifyRow.setText(_translate("viewAll", "Modify Row"))
        self.btnExport.setText(_translate("viewAll", "Export"))
        self.btnAttend.setText(_translate("viewAll", "Attend"))
        self.btnViewAll.setText(_translate("viewAll", "Refresh"))
        self.load_table()


