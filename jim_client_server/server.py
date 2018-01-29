"""Module for creating the server. The server works by protocol TCP through the socket."""

import socket
import json
import argparse
import os
import sys
import logging

from lib import main_loop

parser = argparse.ArgumentParser(description='Server. Author: Ryzhova Tanya')
parser.add_argument('-p', nargs='?', help='Server port')
parser.add_argument('-a', nargs='?', help='IP address for listening')
parser.set_defaults(p='7777', a='0.0.0.0')

args = parser.parse_args()

SERVER_PORT = int(args.p) if args.p is not None else int(parser.get_default('p'))
SERVER_ADDR = args.a if args.a is not None else parser.get_default('a')
NUM_CONNECTIONS = 5
TIMEOUT = 15

prog = \
    {
        "+": (10, 20),
        "-": (35, 3),
        "*": (4.5, 10),
        "/": (9, 4.2)
    }

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)
logging.debug("Create a new TCP-socket.")
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0) as server_sock:
    logging.debug("Bind the socket to address ('%s', '%s').", SERVER_ADDR, SERVER_PORT)
    server_sock.bind((SERVER_ADDR, SERVER_PORT))
    logging.debug("Enable a server to accept connections. "
                  "'%s' unaccepted connections will allow before refusing new connections.", NUM_CONNECTIONS)
    server_sock.listen(NUM_CONNECTIONS)
    logging.debug("Set '%s' seconds on blocking socket operations.", TIMEOUT)
    server_sock.settimeout(TIMEOUT)

    sock, addr = server_sock.accept()
    with sock:
        logging.debug("Connected by '%s'", addr)
        #while True:
        logging.info("The result of calculation is '%s'", main_loop(sock, prog))
