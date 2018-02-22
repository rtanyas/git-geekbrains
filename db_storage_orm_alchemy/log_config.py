import logging
import logging.handlers
import os

from constants import ARTIFACTS_FOLDER_NAME


EXECUTION_LOG_NAME = 'execution_log.log'
STORAGE_FILE = 'storage.txt'
logging.MESSAGE = logging.CRITICAL + 1

class MessageLogger(logging.Logger):

    """Class to add a message log level."""

    logging.addLevelName(logging.MESSAGE, "MESSAGE")

    def message(self, msg, *args, **kwargs):
        """
        Adding a 'message' method to default logging loggers.

        :param msg: Message to log.
        :param args: Additional info required to form a non-standard log.
        :param kwargs: Additional info required to form a non-standard log.
        """
        self.log(logging.MESSAGE, msg, *args, **kwargs)
    logging.Logger.msg = message


def log(func):
    """ Log what function is called. """
    def wrap_log(*args, **kwargs):
        name = func.__name__
        result = func(*args, **kwargs)
        logger = logging.getLogger('root')
        logger.debug("Call function %s with args %s" % (name, args))
        logger.debug("Function %s returned %s" % (name, result))
        return result
    return wrap_log


@log
def setup_custom_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(funcName)s: %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if not os.path.exists(ARTIFACTS_FOLDER_NAME): os.makedirs(ARTIFACTS_FOLDER_NAME)
    log_path = os.path.join(ARTIFACTS_FOLDER_NAME, EXECUTION_LOG_NAME)
    file_handler = logging.handlers.TimedRotatingFileHandler(log_path, when="midnight")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    msg_formatter = logging.Formatter("%(message)s")
    msg_log_path = os.path.join(ARTIFACTS_FOLDER_NAME, STORAGE_FILE)
    msg_file_handler = logging.FileHandler(msg_log_path, mode="a")
    msg_file_handler.setLevel(logging.MESSAGE)
    msg_file_handler.setFormatter(msg_formatter)
    logger.addHandler(msg_file_handler)


setup_custom_logger('root')
#logging.setLoggerClass(MessageLogger)
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.MESSAGE)

