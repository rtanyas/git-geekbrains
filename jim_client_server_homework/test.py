"""Unit tests for testing functions from lib.py. """

import json
import unittest
from unittest.mock import Mock

import lib

class CTestLib(unittest.TestCase):

    def test_div(self):

        res = lib.div(10, 2)
        self.assertEqual(res, 5.0)

        res = lib.div(3.0, 3)
        self.assertEqual(res, 1)

        res = lib.div(6, 2.0)
        self.assertEqual(res, 3.0)

        self.assertRaises(AssertionError, lib.div, 7, 0)
        self.assertRaises(AssertionError, lib.div, "a", 2)
        self.assertRaises(AssertionError, lib.div, 6, "b")

    def test_evl(self):

        res = lib.evl("+", [2, 3])
        self.assertEqual(res, 5.0)

        res = lib.evl("-", [12, 3])
        self.assertEqual(res, 9.0)

        res = lib.evl("*", [2, 7])
        self.assertEqual(res, 14.0)

        self.assertRaises(AssertionError, lib.evl, "%", [2, 3])
        self.assertRaises(AssertionError, lib.evl, "+", ["t", 3])
        self.assertRaises(AssertionError, lib.evl, "-", [4, "k"])

    def test_main_loop(self):

        prog = \
            {
                "+": (10, 20),
                "-": (35, 3),
                "*": (4.5, 10),
                "/": (9, 4.2)
            }

        data = \
            {
                "+": 30,
                "-": 32,
                "*": 45,
                "/": (2.14)

            }
        data = json.dumps(data).encode()

        virt_sock = Mock()
        virt_sock.send.return_value = None
        virt_sock.recv.return_value = data

        res = lib.main_loop(virt_sock, prog)

        self.assertEqual(res["+"], 30)
        self.assertEqual(res["-"], 32)
        self.assertEqual(res["*"], 45)
        self.assertEqual(res["/"], 2.14)

