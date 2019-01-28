import sqlite3
from organisation import Organisation
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class OrganisationRepository:

    selected_code = ''

    def findAll(self):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        query = "select code, name, address from organisations"
        c.execute(query)
        organisations = []
        rows = c.fetchall()
        for row in rows:
            organisation=Organisation(row[0],row[1],row[2])
            organisations.append(organisation)
        connection.close()
        return organisations

    def loadOrgTable(self):

        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        self.orgTable.setRowCount(0)
        query = "select * from organisations"
        results = c.execute(query)
        for row_number, row_data in enumerate(results):
            self.orgTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.orgTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def fetchOrg(code):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        query = "SELECT * FROM organisations where code ='" +  code + "'"
        c.execute(query)
        result = c.fetchone()
        org = Organisation(result[0], result[1], result[2])
        connection.close()
        return org

    def add_org(org):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        query = "INSERT INTO organisations VALUES ('"+ org.code +"','" + org.name +"','" + org.address +"')"
        try:
            c.execute(query)
        except Exception as err:
            print("error msgbox", err)
        connection.commit()
        connection.close()

    def unique(code):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        query = "SELECT CODE FROM organisations"
        c.execute(query)
        result = c.fetchall()
        codes = [i[0] for i in result]
        for c in codes:
            if c == code:
                return False
        return True

    def deleteOrg(code):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        c.execute("DELETE FROM organisations WHERE code='" + code + "'")
        connection.commit()
        connection.close()

    def modOrg(org):
        connection = sqlite3.connect("prg1.db")
        c = connection.cursor()
        query = "UPDATE organisations SET name = '" + org.name + "', address = '" + org.address + "' WHERE CODE = '" \
                   + org.code + "'"
        c.execute(query)
        connection.commit()
        connection.close()








