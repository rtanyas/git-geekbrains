"""Module for creating the server. The server works by protocol TCP through the socket."""

import socket
import json
import argparse
import os
import sys
import logging

from lib import evl

parser = argparse.ArgumentParser(description='Server. Author: Ryzhova Tanya')
parser.add_argument('-p', nargs='?', help='Server port')
parser.add_argument('-a', nargs='?', help='IP address for listening')
parser.set_defaults(p='7777', a='')

args = parser.parse_args()

SERVER_PORT = int(args.p) if args.p is not None else int(parser.get_default('p'))
SERVER_ADDR = args.a if args.a is not None else parser.get_default('a')
NUM_CONNECTIONS = 5
TIMEOUT = 45
BUFSIZE = 1024

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)
logging.debug("Create a new TCP-socket.")
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0) as server_socket:
    logging.debug("Bind the socket to address ('%s', '%s').", SERVER_ADDR, SERVER_PORT)
    server_socket.bind((SERVER_ADDR, SERVER_PORT))
    logging.debug("Enable a server to accept connections. "
                  "'%s' unaccepted connections will allow before refusing new connections.", NUM_CONNECTIONS)
    server_socket.listen(NUM_CONNECTIONS)
    logging.debug("Set '%s' seconds on blocking socket operations.", TIMEOUT)
    server_socket.settimeout(TIMEOUT)

    try:
        while True:
            try:
                sock, client_addr = server_socket.accept()
                with sock:
                    logging.debug("Connection from client is '%s'", client_addr)
                    while True:
                        data = sock.recv(BUFSIZE)
                        if not data:
                            break
                        logging.debug("Receive data '%s' from the socket as '%s'.", data, type(data))
                        data = json.loads(data.decode())
                        logging.debug("Calculating...")
                        result = {}
                        for key in data:
                            result[key] = evl(key, data[key])
                        result = json.dumps(result).encode()
                        sock.send(result)
                        logging.debug("Send data '%s' to the socket as '%s'.", result, type(result))
            except socket.timeout:
                logging.debug("The socket is timed out.")
                server_socket.close()
                break
    except KeyboardInterrupt:
        logging.debug("The server is closing..")
        server_socket.close()
