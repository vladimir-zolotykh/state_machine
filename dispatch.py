#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> conn = Connection()
>>> conn.open()
opened
>>> conn.read()
reading
"""
from enum import Enum


ConnectionState = Enum("ConnectionState", ["OPEN", "CLOSED"])


class ConnectionStateError(Exception):
    pass


class Connection:
    def __init__(self):
        self.state: ConnectionState = ConnectionState.CLOSED

    def open(self):
        if self.state == ConnectionState.CLOSED:
            self.state = ConnectionState.OPEN
            print("opened")
        else:
            raise ConnectionStateError("already open")

    def read(self):
        if self.state == ConnectionState.OPEN:
            print("reading")
        else:
            raise ConnectionStateError("connection not opened")

    def write(self):
        if self.state == ConnectionState.OPEN:
            print("reading")
        else:
            raise ConnectionStateError("connection not opened")

    def close(self):
        if self.state == ConnectionState.OPEN:
            print("close connection")
            self.state == ConnectionState.CLOSED
        else:
            raise ConnectionStateError("can't close closed connection")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
