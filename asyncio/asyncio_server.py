from datetime import datetime
import argparse
import logging
import asyncio
from asyncio.streams import StreamReader, StreamWriter

from storage import SQLiteStorageServerORM
import constants
from init_db import init_database

class AsyncServer(object):
    def __init__(self, server_ip, server_port, db_storage):
        self.clients = set()
        self.server_ip = server_ip
        self.server_port = server_port
        self.db_storage = db_storage
        self.__loop = None

    async def handle_clients(self, reader=StreamReader, writer=StreamWriter):
        self.clients.add(writer)
        while True:
            data = await reader.read(constants.BUFSIZE)
            writer_addr = writer.get_extra_info('peername')
            logger.info("Received data '%s' from '%s'.", data, writer_addr)

            for w in self.clients:
                if w == writer:
                    continue
                w.write(data)
                await w.drain()

            if not data:
                if writer in self.clients:
                    self.clients.remove(writer)
                    try:
                        writer.write_eof()
                    except OSError:
                        pass
                    return

    #async def start_server(self):
        #await asyncio.start_server(self.handle_clients, self.server_ip, self.server_port)

    def run_loop(self):
        self.__loop = asyncio.get_event_loop()

        coro = asyncio.start_server(self.handle_clients, self.server_ip, self.server_port, loop=self.__loop)
        server = self.__loop.run_until_complete(coro)
        logger.info("Serving on '%s'", server.sockets[0].getsockname())

        # server = self.__loop.run_until_complete(self.start_server())

        try:
            self.__loop.run_forever()
        except KeyboardInterrupt:  # Ctrl+C does not work, don't understand why
            server.close()
            self.__loop.run_until_complete(server.wait_closed())
            self.__loop.close()

if __name__ == "__main__":
    logger = logging.getLogger('root')
    init_database(constants.DB_SERVER)

    parser = argparse.ArgumentParser(description='Server. Author: Ryzhova Tanya')
    parser.add_argument('-p', nargs='?', help='Server port')
    parser.add_argument('-a', nargs='?', help='IP address for listening')
    parser.set_defaults(p='7777', a='')
    args = parser.parse_args()
    _SERVER_PORT = int(args.p) if args.p is not None else int(parser.get_default('p'))
    _SERVER_IP = args.a if args.a is not None else parser.get_default('a')
    _DB_STORAGE = SQLiteStorageServerORM("/".join(("sqlite://", constants.ARTIFACTS_FOLDER_NAME, constants.DB_SERVER)))

    AsyncServer(_SERVER_IP, _SERVER_PORT, _DB_STORAGE).run_loop()