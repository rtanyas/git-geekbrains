"""Module for creating the server. The server works by protocol TCP through the socket."""

import socket
import json
import argparse
import logging
import select
from datetime import datetime

from log_config import log, MessageLogger
from storage import FileStorageServer
import constants
from init_db import init_database
import server_answers


@log
class Server(object):

    def _new_listen_tcp_socket(self, server_addr, num_connections, timeout):
        """Create TCP socket for server.

        :param server_address: Tuple containing ip address and port of the server.

        :return: Server socket.
        """
        logger.debug("Create a new TCP-socket for server.")
        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
        server_socket.setblocking(0)
        logger.debug("Bind the socket to address '%s'.", server_addr)
        server_socket.bind((server_addr))
        logger.debug("Enable a server to accept connections. "
                     "'%s' unaccepted connections will allow before refusing new connections.", num_connections)
        server_socket.listen(num_connections)
        logger.debug("Set '%s' seconds on blocking socket operations.", timeout)
        server_socket.settimeout(timeout)
        return server_socket

    def _read_requests(self, clients, all_clients):
        requests = {}
        for sock in clients:
            data = sock.recv(constants.BUFSIZE).decode()
            logger.info("Receive data '%s' from the socket as '%s'.", data, type(data))
#            logger.msg({sock.fileno(): data}, )
            requests[sock] = json.loads(data)
            logger.debug('The client {} disconnected.'.format(sock.fileno()))
            all_clients.remove(sock)
        return all_clients, requests


    def _write_responses(self, requests, clients, all_clients):
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

    def server_mainloop(self, server_addr, num_connections, timeout, file_storage):
        ''' Main loop to work with clients'''
        clients = []
        server_socket = self._new_listen_tcp_socket(server_addr, num_connections, timeout)
        try:
            while True:
                try:
                    conn, client_addr = server_socket.accept()
                    conn.setblocking(0)
                except OSError as e:
                   pass # Timeout is over
                else:
                    logger.debug("New connection with client: %s, %s" % (str(client_addr), conn.fileno()))

                    file_storage.add_client("Client login: {}, client_birthday: {}".format(conn.fileno(), datetime.now()))
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
                    clients_to_response, requests = self._read_requests(readlist, clients)
                    clients = self._write_responses(requests, writelist, clients_to_response)
        except KeyboardInterrupt:
            logging.debug("The server is closing..")
            server_socket.close()


if __name__ == '__main__':
    logger = logging.getLogger('root')
    init_database(constants.DB_SERVER)

    parser = argparse.ArgumentParser(description='Server. Author: Ryzhova Tanya')
    parser.add_argument('-p', nargs='?', help='Server port')
    parser.add_argument('-a', nargs='?', help='IP address for listening')
    parser.set_defaults(p='7777', a='')
    args = parser.parse_args()
    _SERVER_PORT = int(args.p) if args.p is not None else int(parser.get_default('p'))
    _SERVER_IP = args.a if args.a is not None else parser.get_default('a')

    server = Server()
    server.server_mainloop((_SERVER_IP, _SERVER_PORT), constants.NUM_CONNECTIONS, constants.TIMEOUT, FileStorageServer)


