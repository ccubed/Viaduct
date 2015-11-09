# Make our telnet functions into a class. TelServer handles connections, TelHandler is the actual telnet processing.

from telnetsrv.green import TelnetHandler, command
import gevent, gevent.server, Stonework
from cryptography.fernet import Fernet


class UtilException(Exception):
    pass


class TelServer:
    def __init__(self):
        self.connections = 0
        self.users = []

    def new_connection(self, username, phash):
        self.connections += 1
        self.users.append([username, phash])


class TelHandler:
    Server = TelServer()

    WELCOME = "Welcome to Viaduct. Please login."
    PROMPT = ">"
    authNeedUser = True
    authNeedPass = True

    def __init__(self, swref, key):
        self.stoneref = swref
        self.enckey = key

    def authCallback(self, username, password):
        if not username or not password:
            raise UtilException("Either a username or password wasn't specified.")
        else:
            phash = self.stoneref.getpair(username, 4)
            pdata = self.stoneref.gethash(phash, 'all', 0)
            enceng = Fernet(self.enckey)
            if password != enceng.decrypt(pdata[1][1]):
                raise UtilException("Passwords don't match.")

    def session_start(self):
        self.writeline("Welcome back " + self.username)
        phash = self.stoneref.getpair(self.username, 4)
        self.Server.new_connection(self.username, phash)
