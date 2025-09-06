#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> c = Connection()
>>> c._state
<class '__main__.ClosedConnectionState'>
>>> c.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 10, in read
    return self._state.read(self)
  File "example.py", line 43, in read
    raise RuntimeError('Not open')
RuntimeError: Not open
>>> c.open()
>>> c._state
<class '__main__.OpenConnectionState'>
>>> c.read()
reading
>>> c.write('hello')
writing
>>> c.close()
>>> c._state
<class '__main__.ClosedConnectionState'>
>>>
"""
# from abc import ABC, abstractmethod


class Connection:
    def __init__(self):
        self._state: ConnectionState = ClosedConnectionState

    def change_state(self, state):
        self._state = state

    def __getattr__(self, name):
        if name in ("open", "read", "write", "close"):
            return getattr(self._state, name)(self._state)
        raise AttributeError(
            "{!r} object has no attribute {!r}".format(type(self), name)
        )


class ConnectionState:
    @staticmethod
    def open(conn):
        raise RuntimeError()

    @staticmethod
    def read(conn):
        raise RuntimeError()

    @staticmethod
    def write(conn):
        raise RuntimeError()

    @staticmethod
    def close(conn):
        raise RuntimeError()


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def open(conn):
        conn._state.change_state(OpenConnectionState)


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print("reading")

    @staticmethod
    def write(conn):
        print("writing")

    @staticmethod
    def close(conn):
        conn._state.change_state(ClosedConnectionState)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
