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


class CallSuperMeta(type):
    def __new__(cls, name, bases, dct):
        # For each method in the new class...
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                # Wrap it in a function that calls super first
                def make_wrapper(method):
                    def wrapper(self, *args, **kwargs):
                        super_method = getattr(super(type(self), self), method.__name__)
                        super_method(*args, **kwargs)
                        return method(self, *args, **kwargs)

                    return wrapper

                dct[attr_name] = make_wrapper(attr_value)
        return super().__new__(cls, name, bases, dct)


class Connection(Model, metaclass=CallSuperMeta):
    def open(self):
        print("opened")

    def read(self):
        print("reading")

    def write(self):
        print("writing")

    def close(self):
        print("connection closed")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
