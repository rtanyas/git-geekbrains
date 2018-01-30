"""Module for creating the client and connecting to the server. The client works by protocol TCP through the socket."""

import socket
import json
import argparse
import os
import sys
import logging
from random import randint

from lib import main_loop

BUFSIZE = 1024

parser = argparse.ArgumentParser(description='Client. Author: Ryzhova Tanya')
parser.add_argument ('addr', help='Server ip address')
parser.add_argument ('port', nargs='?', help='TCP-port on server')
parser.set_defaults(port='7777')

args = parser.parse_args()

SERVER_ADDR = args.addr
SERVER_PORT = int(args.port) if args.port is not None else int(parser.get_default('port'))
TEST_DATA = \
    {
        "+": (randint(1,10), randint(1,10)),
        "-": (randint(1,10), randint(1,10)),
        "*": (randint(1,10), randint(1,10)),
        "/": (randint(1,10), randint(1,10))
    }

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)
logging.debug("Create a new TCP-socket.")
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0) as client_socket:
    logging.debug("Connect the client socket to server address ('%s', '%s').", SERVER_ADDR, SERVER_PORT)
    client_socket.connect((SERVER_ADDR, SERVER_PORT))
    logging.info("The result of calculation is '%s'", main_loop(client_socket, TEST_DATA))