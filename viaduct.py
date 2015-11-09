# -*- coding: utf-8 -*-

from Stonework import *


if __name__ != '__main__':
    print("Sorry, can't be run as a submodule.")
else:
    RedisConnector = StoneworkC()
    print("Stonework Testing commnecing.")
    RedisConnector.addpair('test', 27, 8)
    print("Added test pair.")
    temp = RedisConnector.getpair('test', 8)
    print(str(temp))

