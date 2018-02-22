from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, Date, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Client(Base):

    __tablename__ = "client"

    gid = Column(Integer(), primary_key=True)
    login = Column(Unicode())
    birthday = Column(Date())

    check_1 = UniqueConstraint("login")

    def __init__(self, login, birthday):
        self.login = login
        self.birthday = birthday

    def __repr__(self):

        return "(id=%d, login=%s, birthday=%s)" % (self.gid, self.login, self.birthday)


class ContactList_(Base):

    __tablename__ = 'contact_list_'

    gid = Column(Integer, primary_key=True)
    phone_number = Column(String)
    address = Column(String)
    client_id = Column(Integer, ForeignKey('client.gid'))

##    client = relationship("Client", foreign_keys=[client_id])

    def __init__(self, phone_number, address, client_id):
        self.phone_number = phone_number
        self.address = address
        self.client_id = client_id

    def __repr__(self):

        return "(client_id=%s, phone=%s, address=%s)" % (self.client_id, self.phone_number, self.address)


class ContactList(Base):

    __tablename__ = 'contact_list'

    gid = Column(Integer, primary_key=True)
    client_id = Column(Integer)

    def __init__(self, client_id):

        self.client_id = client_id

    def __repr__(self):

        return "client_id=%s" % (self.client_id)


class ClientDetails(Base):

    __tablename__ = 'client_details'

    gid = Column(Integer, primary_key=True)
    login_time = Column(DateTime())
    address = Column(String())
    client_id = Column(Integer, ForeignKey('client.gid'))

###    user = relationship("Client", foreign_keys=[client_id])

    def __init__(self, login_time, address, client_id):
        self.login_time = login_time
        self.address = address
        self.client_id = client_id

    def __repr__(self):

        return "client_id=%s, login_time=%s, address=%s" % (self.client_id, self.login_time, self.address)


class Messages(Base):

    __tablename__ = "messages"

    gid = Column(Integer(), primary_key=True)
    from_client = Column(Integer())
    to_client = Column(Integer())
    message = Column(Unicode())

    def __init__(self, from_client, to_client, message):
        self.from_client = from_client
        self.to_client = to_client
        self.message = message

    def __repr__(self):

        return "(%d, %d, %d %s)" % (self.gid, self.from_client, self.to_client, self.message)