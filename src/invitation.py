#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import socket
import threading
from .globals import TCP_PORT, INVITATION_TIMEOUT
from .utils import get_local_ip, receive_and_parse_data

__all__ = [
    "InvitationPacket",
    "InvitationAcceptedPacket",
    "GetConnection",
]


class InvitationPacket:
    """
    Packet sent on invitation request.
    """

    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username


class InvitationAcceptedPacket(InvitationPacket):
    """
    Packet sent on invitation accepted.
    """


class GetConnection(threading.Thread):
    """
    Threaded listener to wait for an invitation request.
    """

    def __init__(self, server):
        threading.Thread.__init__(self)
        self.daemon = True
        self.__is_running = False
        self.__server = server
        self.__connection = None
        self.__username = None
        self.__ip = [get_local_ip(), "127.0.0.1"]

    def run(self):
        self.__is_running = True
        while self.__is_running:
            connection, (ip, _) = self.__server.accept()
            if ip not in self.__ip:
                connection.settimeout(INVITATION_TIMEOUT)
                try:
                    data = receive_and_parse_data(connection, InvitationPacket)
                except (socket.timeout, ConnectionAbortedError):
                    continue

                if data is not None:
                    self.__connection = connection
                    self.__username = data.username
                    while self.__is_running and self.__connection is not None:
                        time.sleep(0.1)
                else:
                    connection.close()

    @property
    def connection(self):
        """
        Get current connection.

        :return: socket connection
        """
        return self.__connection

    @property
    def username(self):
        """
        Get current connection username.

        :return: str, Username
        """
        return self.__username

    @property
    def has_connection(self):
        """
        Check if there is an active connectio

        :return: bool, Has connection
        """
        return self.__connection is not None

    def refuse_connection(self):
        """
        Refuse the current active connection.

        :return: None
        """
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None
            self.__username = None

    def accept_connection(self):
        """
        Accept the current connection and stop the listener.

        :return: None
        """
        if self.__is_running and self.__connection is not None:
            self.__is_running = False

    def stop(self):
        """
        Stop the listener.

        :return: None
        """
        if self.__is_running:
            self.__is_running = False
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("127.0.0.1", TCP_PORT))
