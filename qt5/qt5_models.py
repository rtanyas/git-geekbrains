from PyQt5 import QtCore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm_alchemy import Client, Messages


class ClientListModel(QtCore.QAbstractListModel):

    def __init__(self, param, parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)

        self.__engine = create_engine(param)
        self.__session = sessionmaker(bind=self.__engine)()
        self.refresh()

    def refresh(self):
        self.clients = self.__session.query(Client).all()

    def rowCount(self, parent):
        return len(self.clients)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            value = self.clients[index.row()]
            return value.login
##            return (value.login, value.birthday)


class MessageModel(QtCore.QAbstractListModel):

    def __init__(self, param, parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.__engine = create_engine(param)
        self.__session = sessionmaker(bind=self.__engine)()
        self.refresh()

    def refresh(self):
        self.messages = self.__session.query(Messages).all()

    def rowCount(self, parent):
        return len(self.messages)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            value = self.messages[index.row()]
#            return (value.from_client, value.to_client, value.message)
            return "Message '%s' from client '%s' to client '%s'" % (value.message, value.from_client, value.to_client)