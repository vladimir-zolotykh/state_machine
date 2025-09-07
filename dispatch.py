#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> conn = Connection()
>>> conn.close()
Traceback (most recent call last):
...
ConnectionStateError: connection already closed
>>> conn.read()
Traceback (most recent call last):
...
ConnectionStateError: connection not opened
>>> conn.open()
opened
>>> conn.read()
reading
>>> conn.write()
writing
>>> conn.close()
connection closed
"""
from enum import Enum


ConnectionState = Enum("ConnectionState", ["OPEN", "CLOSED"])


class ConnectionStateError(Exception):
    pass


class Model:
    def __init__(self):
        self.state: ConnectionState = ConnectionState.CLOSED

    def open(self):
        if self.state != ConnectionState.CLOSED:
            raise ConnectionStateError("already open")
        self.state = ConnectionState.OPEN

    def read(self):
        if self.state != ConnectionState.OPEN:
            raise ConnectionStateError("connection not opened")

    def write(self):
        if self.state != ConnectionState.OPEN:
            raise ConnectionStateError("connection not opened")

    def close(self):
        if self.state != ConnectionState.OPEN:
            raise ConnectionStateError("connection already closed")
        self.state = ConnectionState.CLOSED


class Connection(Model):
    def open(self):
        super().open()
        print("opened")

    def read(self):
        super().read()
        print("reading")

    def write(self):
        super().write()
        print("writing")

    def close(self):
        super().close()
        print("connection closed")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
