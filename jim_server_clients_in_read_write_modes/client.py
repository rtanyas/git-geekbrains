"""Module for creating the client and connecting to the server. The client works by protocol TCP through the socket."""

import socket
import json
import argparse
import logging

from log_config import log

parser = argparse.ArgumentParser(description='Client. Author: Ryzhova Tanya')
parser.add_argument('addr', help='Server ip address')
parser.add_argument('port', nargs='?', help='TCP-port on server')
parser.add_argument('-r', '--read_mode', action='store_const', const='1', help='Reading mode')
parser.add_argument('-w', '--write_mode', action='store_const', const='1', help='Writing mode')
parser.set_defaults(port='7777')
args = parser.parse_args()
_SERVER_IP = args.addr
_SERVER_PORT = int(args.port) if args.port is not None else int(parser.get_default('port'))
SERVER_ADDRESS = (_SERVER_IP, _SERVER_PORT)
BUFSIZE = 1024


def read_requests(client_socket):
    while True:
        result = client_socket.recv(BUFSIZE).decode()
        logger.debug("Receive data '%s' from the socket as '%s'.", result, type(result))
        return json.loads(result)


def write_responses(test_data, client_socket):
    data = json.dumps(test_data).encode()
    client_socket.send(data)
    logger.debug("Send data '%s' to the socket as '%s'.", data, type(data))


@log
def client_mainloop():
    try:
        logger.debug("Create a new TCP-socket for client.")
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0) as client_socket:
            logger.debug("Connect the client socket to server address '%s')", SERVER_ADDRESS)
            try:
                client_socket.connect(SERVER_ADDRESS)
            except OSError:
                logger.debug("No connection to server.")
            else:
                if args.read_mode == '1':
                    logger.debug("Client is in listening mode only.")
                    read_requests(client_socket)
                elif args.write_mode == '1':
                    client_message = input("Type in your message: ")
                    logger.debug("Client is in sending mode only.")
                    write_responses(client_message, client_socket)
                else:
                    logger.info("Start client in read or write mode.")
    except KeyboardInterrupt:
        logging.debug("The server is closing..")


if __name__ == '__main__':
    logger = logging.getLogger('root')
    client_mainloop()
