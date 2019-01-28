import sqlite3
from invitee import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
# from viewAll import Ui_viewAll


class InviteeRepository:

    def add(atd):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        insertQuery = "INSERT INTO ATTENDEE (NAME,ORGANISATION,CONTACT) VALUES"
        insertQuery += "('" + atd.name + "','" + atd.organisation + "'," + str(atd.contactNo) + ")"
        c.execute(insertQuery)
        connection.commit()
        connection.close()

    def remove(id):
        connection = sqlite3.connect("prg1.db")
        c=connection.cursor()
        c.execute("DELETE FROM attendee WHERE ID=" + str(id))
        id = None
        connection.commit()
        connection.close()

    def doattend(id):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        c.execute("UPDATE attendee SET attend =1 WHERE id =" + str(id))
        connection.commit()
        connection.close()

    def load_data(self):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        query = "select id, A.name, O.name as Organisation, contact, attend from attendee A JOIN organisations O ON A.organisation=O.code"
        result = c.execute(query)
        self.dataTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.dataTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.dataTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def fetch(id):
        connection = sqlite3.connect("prg1.db")
        c=connection.cursor()
        query = "select id, name, organisation, contact, attend from attendee where id =" + str(id)
        c.execute(query)
        row = c.fetchone()
        print(row)
        inv = Invitee(row[0],row[1],row[2], row[3])
        inv.attend = row[4]
        return inv

    def modify(atd):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        query = "UPDATE attendee SET name ='" + atd.name + "',organisation ='" + atd.organisation + "', contact = "+ str(atd.contactNo) + ", attend ="+ str(atd.attend) +" WHERE ID = " + str(atd.id)
        c.execute(query)
        connection.commit()
        connection.close
