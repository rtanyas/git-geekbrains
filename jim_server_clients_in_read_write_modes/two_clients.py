"""Module for starting two clients in read and write mode under OS Windows."""

from subprocess import Popen, CREATE_NEW_CONSOLE
import logging
from client import SERVER_ADDRESS 

CLIENT_SCRIPT_PATH = "client.py "

common_client_args = ["python ", CLIENT_SCRIPT_PATH, SERVER_ADDRESS[0]]
write_client_mode = [common_client_args, "-w"]
read_client_mode = [common_client_args, "-r"]


logger = logging.getLogger('root')
Popen(read_client_mode, creationflags=CREATE_NEW_CONSOLE)
Popen(write_client_mode, creationflags=CREATE_NEW_CONSOLE)


