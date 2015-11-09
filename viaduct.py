# -*- coding: utf-8 -*-

from Stonework import *


if __name__ != '__main__':
    print("Sorry, can't be run as a submodule.")
else:
    RedisConnector = StoneworkC()
    print("Stonework Testing commnecing.")
    RedisConnector.addpair(1, 27, 8)
    print("Added test pair.")
    temp = RedisConnector.getpair(1, 8)
    print("Value of Pair: " + str(temp, 'utf-8'))
    print("Closing")
    RedisConnector.killkey(1, 8)
