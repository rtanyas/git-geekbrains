"""Module for showing and filtering client messages."""
import sys

from PyQt5 import QtCore, QtWidgets, QtSql

import constants


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent,
            flags = QtCore.Qt.Window)
        self.setWindowTitle("Filtering and sorting messages")

        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName("/".join((constants.ARTIFACTS_FOLDER_NAME, constants.DB_CLIENT)))
        con.open()

##        self.model = QtSql.QSqlQueryModel(parent = self)
##        self.model.setQuery('select * from messages')

        self.model = QtSql.QSqlTableModel(parent = self)
        self.model.setTable('messages')
        self.model.select()

        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'From_client')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'To_client')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'Message')

        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        lblSort = QtWidgets.QLabel("S&ort by field")
        hbox.addWidget(lblSort)

        self.cboSort = QtWidgets.QComboBox()

        message_table = con.record("messages")
        field_count = message_table.count()
        for field in range(0, field_count):
            field_name = message_table.field(field).name()
            if field_name != "gid":
                self.cboSort.addItem(field_name)
        lblSort.setBuddy(self.cboSort)
        hbox.addWidget(self.cboSort)

        self.chkDesc = QtWidgets.QCheckBox("&Descendingly")
        hbox.addWidget(self.chkDesc, alignment = QtCore.Qt.AlignRight)
        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()

        lblFilterSender = QtWidgets.QLabel("Filter by &sender")
        hbox.addWidget(lblFilterSender)
        self.txtFilterSender = QtWidgets.QLineEdit()
        lblFilterSender.setBuddy(self.txtFilterSender)
        hbox.addWidget(self.txtFilterSender)
        vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        lblFilterReceiver = QtWidgets.QLabel("Filter by &recipient")
        hbox.addWidget(lblFilterReceiver)
        self.txtFilterReceiver = QtWidgets.QLineEdit()
        lblFilterReceiver.setBuddy(self.txtFilterReceiver)
        hbox.addWidget(self.txtFilterReceiver)
        vbox.addLayout(hbox)
        btnRefresh = QtWidgets.QPushButton("Re&fresh")
        btnRefresh.clicked.connect(self._refreshData)
        vbox.addWidget(btnRefresh)

        self.tblMain = QtWidgets.QTableView()
        self.tblMain.setModel(self.model)
        self.tblMain.hideColumn(0)
        self.tblMain.setColumnWidth(1, 70)
        self.tblMain.setColumnWidth(2, 70)
        self.tblMain.setColumnWidth(3, 360)
        vbox.addWidget(self.tblMain)
        self.setLayout(vbox)
        self.resize(500, 900)

    """
    def _refreshData(self):
        s = ''
        sender = self.txtFilterSender.text()
        receiver = self.txtFilterReceiver.text()
        if sender and not receiver:
            s += "where from_client like '%" + sender + "%'"
        elif receiver and not sender:
            s += "where to_client like '%" + receiver + "%'"
        elif sender and receiver:
            s += "where from_client like '%" + sender + "%' and to_client like '%" + receiver + "%'"
        s += " order by " + self.cboSort.currentText()
        if self.chkDesc.isChecked():
            s += " desc"
        self.model.setQuery("select * from messages " + s)

    """
    def _refreshData(self):
        sender = self.txtFilterSender.text()
        receiver = self.txtFilterReceiver.text()
        if sender and not receiver:
            self.model.setFilter("from_client like '%" + sender + "%'")
        elif receiver and not sender:
            self.model.setFilter("to_client like '%" + receiver + "%'")
        elif sender and receiver:
            self.model.setFilter("from_client like '%" + sender + "%' and to_client like '%" + receiver + "%'")
        index = self.cboSort.currentIndex()
        self.model.setSort(index+1, QtCore.Qt.AscendingOrder)
        """
        if self.cboSort.currentText() == "from_client":
            self.model.setSort(1, QtCore.Qt.AscendingOrder)
        elif self.cboSort.currentText() == "to_client":
            self.model.setSort(2, QtCore.Qt.AscendingOrder)
        elif self.cboSort.currentText() == "message":
            self.model.setSort(3, QtCore.Qt.AscendingOrder)
         """
        if self.chkDesc.isChecked():
            self.model.setSort(index + 1, QtCore.Qt.DescendingOrder)
        self.model.select()


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
