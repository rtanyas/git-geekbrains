
import json
import logging

BUFSIZE = 1024

def main_loop(sock, test_data):
    """Helper function for sending and receiving data through the socket."""

    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
                        level=logging.DEBUG)
    data = json.dumps(test_data).encode()
    sock.send(data)
    logging.debug("Send data '%s' to the socket as '%s'.", data, type(data))
    result = sock.recv(BUFSIZE)
    logging.debug("Receive data '%s' from the socket as '%s'.", result, type(result))
    return json.loads(result.decode())

def div(x, y):
    """Helper function to divide numbers."""

    assert y != 0, "Divide by 0."
    assert type(x) in [int, float], "Dividend is not a number."
    assert type(y) in [int, float], "Divider is not a number."

    return x / y

def evl(f, ops):
    """Helper function for calculations."""
    funcs = \
        {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : div
        }

    assert f in funcs, "Unknown operation"
    assert type(ops[0]) in [int, float], "Operation not on numbers."
    assert type(ops[1]) in [int, float], "Operation not on numbers."

    return funcs[f](ops[0], ops[1])

