"""Module for creating the client and connecting to the server. The client works by protocol TCP through the socket."""

import socket
import json
import argparse
import logging

from log_config import log, MessageLogger
from storage import SQLiteStorageClientORM, FileStorageClient
import constants
from init_db import init_database
import client_requests
from graphic_chat import ConsoleUI

@log
class Client(object):

    def _read_requests(self, client_socket):
        while True:
            return json.loads(client_socket.recv(constants.BUFSIZE).decode())

    def _write_responses(self, test_data, client_socket):
        client_socket.send(json.dumps(test_data).encode())

    def client_mainloop(self, server_addr, db_storage):
        try:
            logger.debug("Create a new TCP-socket for client.")
            with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0) as client_socket:
                logger.debug("Connect the client socket '%s' to server address '%s'", client_socket.fileno(), server_addr)
                try:
                    client_socket.connect(server_addr)
                except OSError:
                    logger.debug("No connection to server.")
                else:
                    if args.read_mode == '1':
                        logger.debug("Client is in listening mode only.")
                        message = self._read_requests(client_socket)
                        db_storage.save_message('', client_socket.fileno(), message)
                        msgs = db_storage.get_messages_to_client(client_socket.fileno())
                        for msg in msgs:
                            logger.debug("The message '%s' is received from server '%s' to client '%s'.", msg.message, server_addr, msg.to_client)

                            ConsoleUI().display_message(msg.message)

                    elif args.write_mode == '1':
                        logger.debug("Client is in sending mode only.")

                        message = ConsoleUI().input_message

                        db_storage.save_message(client_socket.fileno(), '', message)
                        msgs = db_storage.get_messages_from_client(client_socket.fileno())
                        for msg in msgs:
                            logger.debug("The message '%s' is sent from client '%s' to server '%s'.", msg.message, msg.from_client, server_addr)
                        self._write_responses(message, client_socket)
                    else:
                        logger.info("Start client in read or write mode.")
        except KeyboardInterrupt:
            logging.debug("The server is closing..")

if __name__ == '__main__':
    logger = logging.getLogger('root')
    init_database(constants.DB_CLIENT)

    parser = argparse.ArgumentParser(description='Client. Author: Ryzhova Tanya')
    parser.add_argument('addr', help='Server ip address')
    parser.add_argument('port', nargs='?', help='TCP-port on server')
    parser.add_argument('-r', '--read_mode', action='store_const', const='1', help='Reading mode')
    parser.add_argument('-w', '--write_mode', action='store_const', const='1', help='Writing mode')
    parser.set_defaults(port='7777')
    args = parser.parse_args()
    _SERVER_IP = args.addr
    _SERVER_PORT = int(args.port) if args.port is not None else int(parser.get_default('port'))

    client = Client()
    client.client_mainloop((_SERVER_IP, _SERVER_PORT),
                           SQLiteStorageClientORM("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_CLIENT))))
