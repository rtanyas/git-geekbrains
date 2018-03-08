"""Module for getting client data using PyQt5 Model-View """

import sys

from PyQt5 import QtWidgets, QtSql

from qt5_models import ClientListModel
import constants

def on_clicked():
#    print("Client data:", view1.currentText())
    for sel in view2.selectedIndexes():
        client_id = sel.data()
        print("Client login is '%s'" %client_id)
##        (client_id, client_info) = sel.data()
##        print("Client login is '%s', client's birthday is '%s'" % (client_id, client_info))
    """
    stm = QtSql.QSqlTableModel()
    stm.setTable('client')
    stm.select()
    rec = con.record('client')
    rec.setValue('to_client', to_client)
    rec.setValue('message', msg)
    stm.insertRecord(-1, rec)
    """
    """
    query = QtSql.QSqlQuery()
    con.transaction()
    query.prepare("insert into contact_list value(null, :client_id)")
    query.bindValue(':client_id', client_id)

    query.exec_()
    con.commit()
    """

##con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
##con.setDatabaseName("/".join((constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER)))
##con.open()

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("Server")
window.resize(300, 200)

#view1 = QtWidgets.QComboBox(window)
#view1.setModel(ClientListModel("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER))))
view2 = QtWidgets.QListView()
view2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
view2.setModel(ClientListModel("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER))))

button = QtWidgets.QPushButton("Get the client data.")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
#box.addWidget(view1)
box.addWidget(view2)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())