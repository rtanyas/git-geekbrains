import argparse
import logging
from functools import wraps

import asyncio

from log_config import log
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

#@_login_required
@log
class AsyncClient(object):
    def __init__(self, server_ip, server_port, db_storage):
        self.server_ip = server_ip
        self.server_port = server_port
        self.db_storage = db_storage
        self.__loop = None

    async def tcp_client(self, loop):
        try:
            logger.info("Connecting to %s:%d" % (self.server_ip, self.server_port))
            reader, writer = await asyncio.open_connection(self.server_ip, self.server_port, loop=self.__loop)
            logger.debug("Connected to server %s:%d." % (self.server_ip, self.server_port))
            if args.read_mode == '1':
                logger.debug("Client is in the listening mode only.")
                while True:
                    message = await reader.read(constants.BUFSIZE)
                    logger.info("The message '%s' is received." % message.decode())

                    self.db_storage.save_message('', 'reader_test', message)
                    self.db_storage.get_messages_to_client('reader_test')
                    ConsoleUI().display_message(message)
            elif args.write_mode == '1':
                logger.debug("Client is in the sending mode only.")
                while True:
                    message = ConsoleUI().input_message
                    logger.info('Sent: %s' % message)

                    self.db_storage.save_message('writer_test', '', message)
                    self.db_storage.get_messages_from_client('writer_test')
                    writer.write(message.encode())
                    #logger.debug('Close the socket')
                    #writer.close()
        except ConnectionRefusedError:
            logger.info("No connection to server.")

    def run_loop(self):
        self.__loop = asyncio.get_event_loop()
        self.__loop.run_until_complete(self.tcp_client(self.__loop))
        try:
            self.__loop.run_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    logger = logging.getLogger('root')
    init_database(constants.DB_SERVER)
    init_database(constants.DB_CLIENT)

    parser = argparse.ArgumentParser(description='Client. Author: Ryzhova Tanya')
    parser.add_argument('addr', help='Server ip address')
    parser.add_argument('port', nargs='?', help='TCP-port on server')
    parser.add_argument('-r', '--read_mode', action='store_const', const='1', help='Reading mode')
    parser.add_argument('-w', '--write_mode', action='store_const', const='1', help='Writing mode')

    parser.add_argument("--login", help="Login") # required=True
    parser.add_argument("--level", help="Level") # required=True
    parser.add_argument("--password", help="Password") # required=True

    parser.set_defaults(port='7777')
    args = parser.parse_args()
    _SERVER_IP = args.addr
    _SERVER_PORT = int(args.port) if args.port is not None else int(parser.get_default('port'))

    _USER_LOGIN = args.login
    _USER_LEVEL = args.level
    _USER_PASSWORD = args.password

    _DB_SERVER_STORAGE = SQLiteStorageServerORM("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER)))
    _DB_CLIENT_STORAGE = SQLiteStorageClientORM("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_CLIENT)))

    #password_hash = generate_hash.get_hash(args.login, args.level, args.password)
    #_DB_SERVER_STORAGE.save_auth_data(args.login, args.level, password_hash)

    AsyncClient(_SERVER_IP, _SERVER_PORT, _DB_CLIENT_STORAGE).run_loop()