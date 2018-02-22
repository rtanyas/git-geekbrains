import abc


class UI(object):
    """Base class for creating UI(User Interface)."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def display_message(self, msg):
        pass

    @abc.abstractmethod
    def input_message(self):
        pass


class ConsoleUI(UI):

    def __init__(self):
        super().__init__()

    def display_message(self, msg):
        print("You received the message: ", msg)

    @property
    def input_message(self):
        return input("Type in your message please: ")

