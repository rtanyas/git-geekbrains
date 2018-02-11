"""Module for creating the server. The server works by protocol TCP through the socket."""

import socket
import json
import argparse
import logging
import select

from log_config import log

parser = argparse.ArgumentParser(description='Server. Author: Ryzhova Tanya')
parser.add_argument('-p', nargs='?', help='Server port')
parser.add_argument('-a', nargs='?', help='IP address for listening')
parser.set_defaults(p='7777', a='')

args = parser.parse_args()

_SERVER_PORT = int(args.p) if args.p is not None else int(parser.get_default('p'))
_SERVER_IP = args.a if args.a is not None else parser.get_default('a')
SERVER_ADDRESS = (_SERVER_IP, _SERVER_PORT)
NUM_CONNECTIONS = 5
TIMEOUT = 15
BUFSIZE = 1024


def new_listen_tcp_socket(server_address):
    """Create TCP socket for server.
    
    :param server_address: Tuple containing ip address and port of the server.
    
    :return: Server socket. 
    """
    logger.debug("Create a new TCP-socket for server.")
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    server_socket.setblocking(0)
    logger.debug("Bind the socket to address '%s'.", SERVER_ADDRESS)
    server_socket.bind((server_address))
    logger.debug("Enable a server to accept connections. "
                  "'%s' unaccepted connections will allow before refusing new connections.", NUM_CONNECTIONS)
    server_socket.listen(NUM_CONNECTIONS)
    logger.debug("Set '%s' seconds on blocking socket operations.", TIMEOUT)
    server_socket.settimeout(TIMEOUT)
    return server_socket


def read_requests(clients, all_clients):
    requests = {}
    for sock in clients:
        data = sock.recv(1024).decode()
        logger.info("Receive data '%s' from the socket as '%s'.", data, type(data))
        requests[sock] = json.loads(data)
        logger.debug('The client {} disconnected.'.format(sock.fileno()))
        all_clients.remove(sock)
    return all_clients, requests


def write_responses(requests, clients, all_clients):
    for sock in clients:
        if sock in requests:
            data = json.dumps(requests[sock]).encode()
            for i_sock in all_clients:
                try: 
                    i_sock.send(data)
                    logger.debug("Send data '%s' to the socket as '%s'.", data, type(data))
                    logger.debug('The client {} disconnected.'.format(i_sock.fileno()))
                    all_clients.remove(i_sock)
                except BrokenPipeError:
                    logger.debug('No clients')
    return all_clients


@log
def server_mainloop():
    ''' Main loop to work with clients'''
    clients = []
    server_socket = new_listen_tcp_socket(SERVER_ADDRESS)
    try:
        while True:
            try:
                conn, client_addr = server_socket.accept()
                conn.setblocking(0)
            except OSError as e:               
               pass # Timeout is over
            else:
                logger.debug("New connection with client: %s, %s" % (str(client_addr), conn.fileno()))
                clients.append(conn)
                logger.debug("{} clients are connected to the server".format(len(clients)))
            finally:
                readlist = []
                writelist = []
                try:
                    readlist, writelist, _ = select.select(clients, clients, [], 0)
                    logger.debug("There are {} clients in the readlist".format(len(readlist)))
                    logger.debug("There are {} clients in the writelist".format(len(writelist)))
                except OSError:
                    pass
                clients_to_response, requests = read_requests(readlist, clients)
                clients = write_responses(requests, writelist, clients_to_response)
    except KeyboardInterrupt:
        logging.debug("The server is closing..")
        server_socket.close()

if __name__ == '__main__':
    logger = logging.getLogger('root')
    server_mainloop()
