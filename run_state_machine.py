#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> c = Connection()
>>> c._state
<class '__main__.ClosedConnectionState'>
>>> c.open()
>>> c._state
<class '__main__.OpenConnectionState'>
>>> c.read()
reading
>>> c.read()
reading
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

    def open(self):
        self._state.open(self)

    def read(self):
        self._state.read(self)

    def write(self):
        self._state.write(self)

    def close(self):
        self._state.close(self)


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
    def open(conn: Connection):
        assert isinstance(conn, Connection)
        conn.change_state(OpenConnectionState)


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print("reading")

    @staticmethod
    def write(conn):
        print("writing")

    @staticmethod
    def close(conn):
        conn.change_state(ClosedConnectionState)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
