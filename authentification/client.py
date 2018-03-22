"""Module for creating the client and connecting to the server. The client works by protocol TCP through the socket."""

import socket
import json
import argparse
import logging
import sys
from functools import wraps

from log_config import log, MessageLogger
from storage import SQLiteStorageClientORM, SQLiteStorageServerORM
import constants
from init_db import init_database
from graphic_chat import ConsoleUI
import generate_hash

def _login_required(method):
    @wraps(method)
    def wrap(*args, **kwargs):
        pass_hash = generate_hash.get_hash(_USER_LOGIN, _USER_LEVEL, _USER_PASSWORD)
        user_login_from_db = _DB_SERVER_STORAGE.get_user_login(_USER_LOGIN, _USER_LEVEL, pass_hash)
        if user_login_from_db:
            print("Login success")
            return method(*args, **kwargs)
        print("You have a problem with authentification!")
    return wrap

@log
class Client(object):

    def _read_requests(self, client_socket):
        while True:
            return json.loads(client_socket.recv(constants.BUFSIZE).decode())

    def _write_responses(self, test_data, client_socket):
        client_socket.send(json.dumps(test_data).encode())

    @_login_required
    def client_mainloop(self, server_addr, db_storage):
        logger.debug("Try to create a new TCP-socket for client.")
        try:
            with socket.create_connection(server_addr, constants.CLIENT_CONNECT_TIMEOUT) as client_socket:
                client_socket.settimeout(constants.CLIENT_READ_TIMEOUT)  # set socket read timeout
                logger.debug("There is a connection to server.")
                if args.read_mode == '1':
                    logger.debug("Client is in listening mode only.")
                    message = self._read_requests(client_socket)
                    db_storage.save_message('', client_socket.fileno(), message)
                    msgs = db_storage.get_messages_to_client(client_socket.fileno())
                    for msg in msgs:
                        logger.debug("The message '%s' is received from server '%s' to client '%s'.", msg.message,
                                     server_addr, msg.to_client)

                        ConsoleUI().display_message(msg.message)

                elif args.write_mode == '1':
                    logger.debug("Client is in sending mode only.")

                    message = ConsoleUI().input_message

                    db_storage.save_message(client_socket.fileno(), '', message)
                    msgs = db_storage.get_messages_from_client(client_socket.fileno())
                    for msg in msgs:
                        logger.debug("The message '%s' is sent from client '%s' to server '%s'.", msg.message,
                                    msg.from_client, server_addr)
                    self._write_responses(message, client_socket)
                else:
                    logger.info("Start client in read or write mode.")
        ##        except OSError:
        except ConnectionRefusedError:
            logger.info("No connection to server.")
        except socket.timeout:
            logger.info("Timeout is over.")
        except KeyboardInterrupt:
            logging.debug("The client is closing..")
            client_socket.close()
            sys.exit()

if __name__ == '__main__':
    logger = logging.getLogger('root')
    init_database(constants.DB_SERVER)
    init_database(constants.DB_CLIENT)

    parser = argparse.ArgumentParser(description='Client. Author: Ryzhova Tanya')
    parser.add_argument('addr', help='Server ip address')
    parser.add_argument('port', nargs='?', help='TCP-port on server')
    parser.add_argument('-r', '--read_mode', action='store_const', const='1', help='Reading mode')
    parser.add_argument('-w', '--write_mode', action='store_const', const='1', help='Writing mode')

    parser.add_argument("--login", help="Login", required=True)
    parser.add_argument("--level", help="Level", required=True)
    parser.add_argument("--password", help="Password", required=True)

    parser.set_defaults(port='7777')
    args = parser.parse_args()
    _SERVER_IP = args.addr
    _SERVER_PORT = int(args.port) if args.port is not None else int(parser.get_default('port'))

    _USER_LOGIN = args.login
    _USER_LEVEL = args.level
    _USER_PASSWORD = args.password

    _DB_SERVER_STORAGE = SQLiteStorageServerORM("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER)))
    _DB_CLIENT_STORAGE = SQLiteStorageClientORM("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_CLIENT)))

#    password_hash = generate_hash.get_hash(args.login, args.level, args.password)
#    _DB_SERVER_STORAGE.save_auth_data(args.login, args.level, password_hash)

    client = Client()
    client.client_mainloop((_SERVER_IP, _SERVER_PORT), _DB_CLIENT_STORAGE)