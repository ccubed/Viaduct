# Unit Tests

import unittest
from Backend import *
import simplejson as json
from Web import *
from gevent import pywsgi
from gevent import socket
import redis

class StoneworkUnits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Stoneref = Stonework()

    def test_badDbHash(self):
        self.assertEqual(self.Stoneref.addhash(1024, {'Test': 'True'}, 22), 0)

    def test_badDbPair(self):
        self.assertEqual(self.Stoneref.addpair(1, 10, 22), 0)

    def test_addHash(self):
        self.assertTrue(self.Stoneref.addhash(1024, {'Test': 'True'}, 1))

    def test_addPair(self):
        self.assertTrue(self.Stoneref.addpair(1, 10, 8))

    def test_getPair(self):
        self.assertEqual(self.Stoneref.getpair(1, 8), '10')

    def test_killKey(self):
        self.assertTrue(self.Stoneref.killkey(1, 8))

    def test_badDbKillKey(self):
        self.assertFalse(self.Stoneref.killkey(1, 22))

    def test_jsonHash(self):
        json.loads(self.Stoneref.gethash(1024, 'Test', 1, 'json'))

    def test_pythonHash(self):
        self.assertEqual(self.Stoneref.gethash(1024, 'Test', 1, 'python'), 'True')

    def test_textHash(self):
        self.assertEqual(self.Stoneref.gethash(1024, 'Test', 1, 'text'), 'True')

    def test_jsonHashAll(self):
        json.loads(self.Stoneref.gethash(1024, 'all', 1, 'json'))

    def test_pythonHashAll(self):
        self.assertDictEqual(self.Stoneref.gethash(1024, 'all', 1, 'python'), {b'Test': b'True'})

    def test_textHashAll(self):
        self.Stoneref.gethash(1024, 'all', 1, 'text')

    # Just making sure this runs last
    def test_xkillKeyHash(self):
        self.Stoneref.killkey(1024, 1)

    def test_dump(self):
        self.Stoneref.redisdump()
        
    def test_autoExpire2(self):
        self.Stoneref.addhash(1025, {'test': 1}, 2)
    
    def test_autoExpire11(self):
        self.Stoneref.addhash(1026, {'test': 1}, 11)
        
    #TODO: Figure out why this fails.
    #def test_autoExpire15(self):
    #    self.Stoneref.addhash(1027, {'test': 1}, 15)

class WebUnits(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        self.server = Webserver(Stonework())
        self.instance = pywsgi.WSGIServer(('0.0.0.0',8443), self.server.responseHandler)
        self.instance.start()
        
    def test_apiTest(self):
        value = redis.StrictRedis(host='localhost',port=6379,db=8)
        value.set('test',22)
        connection = socket.create_conection(('127.0.0.1',8443))
        connection.sendall('GET /api/pair/test')
        data = connection.recv(4096)
        value.expire('test',8)
        assertEqual(str(data,'utf-8'),'22')