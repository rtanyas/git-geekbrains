# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtSql, QtCore
import sys

from qt5_models import MessageModel, ClientListModel
import constants


def on_add_contact():
    contact, ok = QtWidgets.QInputDialog.getText(window, "Adding contact",
                                       "Add new contact to your local contact list",
                                       text="")
    if ok:
        print("New contact is:", contact)

        stm = QtSql.QSqlTableModel()
        stm.setTable('client_contact_list')
        stm.select()
        rec = con.record('client_contact_list')
        rec.setValue('contact', contact)
        stm.insertRecord(-1, rec)

def on_send_message():
    for sel in view.selectedIndexes():
        client_login = sel.data()
        print(sel.data())
##        (client_login, client_info) = sel.data()
        print("You are going to send a message to the client:", client_login)

    msg, ok = QtWidgets.QInputDialog.getText(window, "Sending messages",
                                       "Type in your message for chosen client",
                                       text="Default text message for the client '%s'" %client_login)
    if ok:
        print("Your message is:", msg)

        stm = QtSql.QSqlTableModel()
        stm.setTable('messages')
        stm.select()
        rec = con.record('messages')
        rec.setValue('from_client', '1122')
        rec.setValue('to_client', client_login)
        rec.setValue('message', msg)
        stm.insertRecord(-1, rec)
        """
        query = QtSql.QSqlQuery()
        con.transaction()
        if 'messages' not in con.tables():
            query = QtSql.QSqlQuery()
            query.exec(
                "create table messages(gid integer primary key autoincrement, from_client integer, to_client integer, message text)")


        query.prepare("insert into messages values(null, :from_client, :to_client, :message)")
        query.bindValue(':from_client', '')
        query.bindValue(':to_client', client_login)
        query.bindValue(':message', msg)
        query.exec_()
        con.commit()
        """

con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName("/".join((constants.ARTIFACTS_FOLDER_NAME, constants.DB_CLIENT)))
con.open()

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("Client")
window.resize(300, 100)

view = QtWidgets.QListView()
view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
view.setModel(ClientListModel("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER))))


button_1 = QtWidgets.QPushButton("Send message for chosen client")
button_1.clicked.connect(on_send_message)

button_2 = QtWidgets.QPushButton("Add contact to your contact list")
button_2.clicked.connect(on_add_contact)

box = QtWidgets.QVBoxLayout()

box.addWidget(view)
box.addWidget(button_1)
box.addWidget(button_2)
window.setLayout(box)
window.show()

sys.exit(app.exec_())
con.close()