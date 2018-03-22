import sqlite3
import logging
from abc import abstractmethod

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from log_config import MessageLogger
from orm_alchemy import Client, ContactList, ClientDetails, Messages, Auth


class BaseStorageClient:

    @abstractmethod
    def save_message(self, from_client, to_client, message): pass

    @abstractmethod
    def get_messages_from_client(self, login): pass

    @abstractmethod
    def get_messages_to_client(self, login): pass


class SQLiteStorageClient(BaseStorageClient):

    def __init__(self, param):

        self.__conn = sqlite3.connect(param)
        self.__cursor = self.__conn.cursor()

    def save_message(self, from_client, to_client, message):

        self.__cursor.execute("insert into messages (from_client, to_client, message) values (%d, %d, '%s')" % (from_client, to_client, message))

    def get_messages_from_client(self, login):

        self.__cursor.execute("select * from messages where from_client = %d" % login)
        return self.__cursor.fetchall()

    def get_messages_to_client(self, login):

        self.__cursor.execute("select * from messages where to_client = %d" % login)
        return self.__cursor.fetchall()

    def get_all_messages(self):

        self.__cursor.execute("select * from messages")
        return self.__cursor.fetchall()


class SQLiteStorageClientORM(BaseStorageClient):

    def __init__(self, param):
        self.__engine = create_engine(param)
        self.__session = sessionmaker(bind=self.__engine)()

    def save_message(self, from_client, to_client, message):
        self.__session.add(Messages(from_client, to_client, message))
        self.__session.commit()

    def get_messages_from_client(self, login):
        return self.__session.query(Messages).filter(Messages.from_client == login).all()

    def get_messages_to_client(self, login):
        return self.__session.query(Messages).filter(Messages.to_client == login).all()


class BaseStorageServer:

    @abstractmethod
    def add_client(self, login, birthday): pass

    @abstractmethod
    def get_all_clients(self): pass


class SQLiteStorageServer(BaseStorageServer):

    def __init__(self, param):

        self.__conn = sqlite3.connect(param)
        self.__cursor = self.__conn.cursor()

    def add_client(self, login, birthday):
        pass

    def get_all_clients(self):

        self.__cursor.execute("select * from client")
        return self.__cursor.fetchall()


class SQLiteStorageServerORM(BaseStorageServer):

    def __init__(self, param):

        self.__engine = create_engine(param)
        self.__session = sessionmaker(bind=self.__engine)()

    def add_client(self, login, birthday):

        client = self.__session.query(Client).filter(Client.login == login).first()
        if not client:
            self.__session.add(Client(login, birthday))
            self.__session.commit()

    def add_client_details(self, login_time, address, client_id):

        client_details = ClientDetails(login_time, address, client_id)
        self.__session.add(client_details)
        self.__session.commit()

    def get_client_details(self, client_id):

        return self.__session.query(ClientDetails).filter(ClientDetails.client_id == client_id).first()

    def get_client_id_by_login(self, login):

        client = self.__session.query(Client).filter(Client.login == login).first()
        return client.gid

    def delete_client(self, login):

        self.__session.query(Client).filter(Client.login == login).delete()
        self.__session.commit()

    def get_all_clients(self):

        return self.__session.query(Client).all()

    def get_contact(self, client_id):

        return self.__session.query(ContactList).filter(ContactList.client_id == client_id).first()

    def get_all_contacts(self):

        return self.__session.query(ContactList).all()

#    def add_contact(self, phone_number, address, client_id):
#
#        client = self.__session.query(Client).get(client_id)
#        client_contact = ContactList(phone_number, address, client)
#        self.__session.add(client_contact)
#        self.__session.commit()

    def add_contact(self, client_id):

        contact = self.__session.query(ContactList).filter(ContactList.client_id == client_id).first()
        if not contact:
            self.__session.add(ContactList(client_id))
            self.__session.commit()

    def del_contact(self, client_id):
        self.__session.query(ContactList).filter(ContactList.client_id == client_id).delete()
        self.__session.commit()

    def save_auth_data(self, user_login, user_level, password_hash):
        self.__session.add(Auth(user_login, user_level, password_hash))
        self.__session.commit()

    def get_user_login(self, user_login, user_level, pass_hash):
        user = self.__session.query(Auth).filter(Auth.user_login == user_login).filter(Auth.user_level == user_level).filter(Auth.pass_hash == pass_hash).first()
        if user:
            return user.user_login

    def get_pass_hash(self, user_login, user_level, pass_hash):
        user = self.__session.query(Auth).filter(Auth.user_login == user_login).filter(Auth.user_level == user_level).filter(Auth.pass_hash == pass_hash).first()
        if user:
            return user.pass_hash


class FileStorageServer(BaseStorageServer):
    def add_client(client_info):
        logging.setLoggerClass(MessageLogger)
        logger = logging.getLogger('root')
        logger.setLevel(logging.MESSAGE)
        logger.msg(client_info)

class FileStorageClient(BaseStorageClient):

    def save_message(message):
        logging.setLoggerClass(MessageLogger)
        logger = logging.getLogger('root')
        logger.setLevel(logging.MESSAGE)
        logger.msg(message)


logger = logging.getLogger('root')