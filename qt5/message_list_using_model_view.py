"""Module for getting client messages using PyQt5 Model-View """

import sys

from PyQt5 import QtWidgets

from qt5_models import MessageModel
import constants

def on_clicked():

    for sel in view.selectedIndexes():
        print(sel.data())

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("Messages in QListView")
window.resize(500, 500)

view = QtWidgets.QListView()
view.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
view.setModel(MessageModel("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_CLIENT))))

button = QtWidgets.QPushButton("Take the message.")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())