import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets

#import db_manager as db
import qt5_fonts_smiles as qt5_client
import render_image


class Ui_login_dialog_widget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
#        self.dbu = db.DatabaseUtility(os.path.join(constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER), 'auth')
        self.setupUi(self)
        self.confirm = None

    def setupUi(self, login_dialog_widget):
        login_dialog_widget.setObjectName("login_dialog_widget")
        self.setGeometry(300, 300, 500, 270)
        self.layoutWidget = QtWidgets.QWidget(login_dialog_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 425, 257))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.foto_button = QtWidgets.QPushButton(self.layoutWidget)
        self.foto_button.setObjectName("foto_button")
        self.horizontalLayout_3.addWidget(self.foto_button)
        self.image_label = QtWidgets.QLabel(self.layoutWidget)
        self.image_label.setText("")

        self.image_label.setObjectName("image_label")
        self.horizontalLayout_3.addWidget(self.image_label)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.user_label = QtWidgets.QLabel(self.layoutWidget)
        self.user_label.setObjectName("user_label")
        self.verticalLayout_2.addWidget(self.user_label)
        self.user_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_lineEdit.setSizeIncrement(QtCore.QSize(100, 0))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.verticalLayout_2.addWidget(self.user_lineEdit)
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setObjectName("password_label")
        self.verticalLayout_2.addWidget(self.password_label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_lineEdit.setSizeIncrement(QtCore.QSize(100, 0))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout_2.addWidget(self.password_lineEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sign_in_button = QtWidgets.QPushButton(self.layoutWidget)
        self.sign_in_button.setObjectName("sign_in_button")
        self.horizontalLayout.addWidget(self.sign_in_button)
        spacerItem2 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.login_button = QtWidgets.QPushButton(self.layoutWidget)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.cancel_button = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(login_dialog_widget)
        QtCore.QMetaObject.connectSlotsByName(login_dialog_widget)

    def retranslateUi(self, login_dialog_widget):
        _translate = QtCore.QCoreApplication.translate
        login_dialog_widget.setWindowTitle(_translate("login_dialog_widget", "User login form"))
        self.foto_button.setText(_translate("login_dialog_widget", "Add foto"))
        self.user_label.setText(_translate("login_dialog_widget", "Username"))
        self.password_label.setText(_translate("login_dialog_widget", "Password"))
        self.sign_in_button.setText(_translate("login_dialog_widget", "Sign in"))
        self.login_button.setText(_translate("login_dialog_widget", "Login"))
        self.cancel_button.setText(_translate("login_dialog_widget", "Cancel"))

        self.sign_in_button.clicked.connect(self.NewUser_btn)
        self.cancel_button.clicked.connect(self.Cancel_btn)
        self.login_button.clicked.connect(self.Login_btn)
        self.foto_button.clicked.connect(self.showDialog)

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]
#        pixmap = QtGui.QPixmap(fname) # without foto changings
        pixmap = QtGui.QPixmap.fromImage(render_image.render(fname, 'gray')) # 'gray', 'negative', 'bw', 'sepia'
        self.image_label.setPixmap(pixmap)

    def Cancel_btn(self):
        self.close()

    def Login_btn(self):
        username = self.user_lineEdit.text()
        password = self.password_lineEdit.text()
        if not username:
            QtWidgets.QMessageBox.warning(self, 'Warning!', 'Username is missing')
        elif not password:
            QtWidgets.QMessageBox.warning(self, 'Warning!', 'Password is missing')
        else:
            self.AttemptLogin(username, password)

    def NewUser_btn(self):
        self.newUser = Ui_Register_Dialog()
#        self.newUser = Ui_Register_Dialog(self.dbu)
        self.newUser.show()

    def AttemptLogin(self, username, password):
        # TODO: add authentification
        self.contacts = qt5_client.Window()
        self.contacts.show()
        self.close()

class Ui_Register_Dialog(QtWidgets.QWidget):
    def __init__(self):
#    def __init__(self, dbu):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
#        self.dbu = dbu

    def setupUi(self, Register_Dialog):
        Register_Dialog.setObjectName("Register_Dialog")
        self.setGeometry(300, 300, 450, 250)
#        Register_Dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Register_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Register_Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_lineEdit = QtWidgets.QLabel(self.groupBox)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.username_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.confirmPassword_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.confirmPassword_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword_lineEdit.setObjectName("confirmPassword_lineEdit")
        self.horizontalLayout_4.addWidget(self.confirmPassword_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Register_Dialog)

    def retranslateUi(self, Register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Register_Dialog.setWindowTitle(_translate("Register_Dialog", "Register new user"))
        self.user_lineEdit.setText(_translate("Register_Dialog", "Username"))
        self.label.setText(_translate("Register_Dialog", "Password"))
        self.label_3.setText(_translate("Register_Dialog", "Confirm Password"))
        self.add_btn.setText(_translate("Register_Dialog", "Add"))
        self.cancel_btn.setText(_translate("Register_Dialog", "Cancel"))

        self.add_btn.clicked.connect(self.Add_btn)
        self.cancel_btn.clicked.connect(self.Cancel_btn)

    def Cancel_btn(self):
        self.close()

    def Add_btn(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        cpassword = self.confirmPassword_lineEdit.text()
        if not username or not password:
            QtWidgets.QMessageBox.warning(self, 'Warning!', 'Username or password is missing')
        elif password != cpassword:
            QtWidgets.QMessageBox.warning(self, 'Warning!', 'Passwords do not match')
        else:
            # TODO: Check the existence of the user in the database
#            self.dbu.AddEntryToTable(username, password)
            QtWidgets.QMessageBox.information(self, 'Awesome!', 'User is added successfully!')
            self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_login_dialog_widget()
    ex.show()
    sys.exit(app.exec_())
