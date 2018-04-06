# -*- coding: utf-8 -*-
import sys
import os

from PyQt5 import QtWidgets, QtSql, QtCore, QtGui

IMAGES_FOLDER_NAME = 'images'


class FormatText(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)

        toolbar = self.addToolBar('Formatting')
        name_to_icon = {'Bold': 'b.jpg', 'Italic': 'i.jpg', 'Underlined': 'u.jpg', 'Color': 'red.jpg',
                        'Smile': 'ab.gif', 'Melancholy': 'ac.gif', 'Surprise': 'ai.gif'}
        for action_name, icon_file_name in name_to_icon.items():
            action_name = QtWidgets.QAction(QtGui.QIcon(os.path.join(IMAGES_FOLDER_NAME, icon_file_name)),
                                            action_name, self)
            action_name.triggered.connect(self.on_action)
            toolbar.addAction(action_name)

    def on_action(self):
        cursor = self.textEdit.textCursor()
        text = cursor.selectedText()
        sender = self.sender()
        print(sender.text())
        self.statusBar().showMessage('"{}" was chosen'.format(sender.text()))
        f = QtGui.QTextCharFormat()
        if sender.text() == 'Bold':
            self.textEdit.setFontWeight(QtGui.QFont.Bold)
            self.textEdit.insertHtml('<b>%s</b>' % text)
        elif sender.text() == 'Italic':
            f.setFontItalic(True)
            self.textEdit.setCurrentCharFormat(f)
            self.textEdit.insertHtml('<i>%s</i>' % text)
        elif sender.text() == 'Underlined':
            f.setFontUnderline(True)
            self.textEdit.setCurrentCharFormat(f)
            self.textEdit.insertHtml('<u>%s</u>' % text)
        elif sender.text() == 'Color':
            self.textEdit.insertHtml('<font color=red>%s</font>' % text)
        elif sender.text() == 'Smile':
            self.textEdit.insertHtml('<img src="%s" />' % 'ab.gif')
        elif sender.text() == 'Melancholy':
            self.textEdit.insertHtml('<img src="%s" />' % 'ac.gif')
        elif sender.text() == 'Surprise':
            self.textEdit.insertHtml('<img src="%s" />' % 'ai.gif')

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Client')
        self.setWindowIcon(QtGui.QIcon(os.path.join(IMAGES_FOLDER_NAME, 'red.jpg')))

        self.view = FormatText()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.view)
        self.setLayout(vbox)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())