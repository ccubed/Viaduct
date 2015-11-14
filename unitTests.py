# Unit Tests

import unittest

from Backend import *


class StoneworkUnits(unittest.TestCase):
    def test_badDbHash(self):
        self.assertEqual(addhash(1024, {'Test': 'True'}, 22), 0)

    def test_badDbPair(self):
        self.assertEqual(addpair(1, 10, 22), 0)

    def test_addHash(self):
        self.assertTrue(addhash(1024, {'Test': 'True'}, 1))

    def test_addPair(self):
        self.assertTrue(addpair(1, 10, 8))

    def test_getPair(self):
        self.assertEqual(getpair(1, 8), '10')

    def test_killKey(self):
        self.assertTrue(killkey(1, 8))

    def test_badDbKillKey(self):
        self.assertFalse(killkey(1, 22))

    def test_jsonHash(self):
        json.loads(gethash(1024, 'Test', 1, 'json'))

    def test_pythonHash(self):
        self.assertEqual(gethash(1024, 'Test', 1, 'python'), 'True')

    def test_textHash(self):
        self.assertEqual(gethash(1024, 'Test', 1, 'text'), 'True')

    def test_jsonHashAll(self):
        json.loads(gethash(1024, 'all', 1, 'json'))

    def test_pythonHashAll(self):
        self.assertDictEqual(gethash(1024, 'all', 1, 'python'), {b'Test': b'True'})

    def test_textHashAll(self):
        gethash(1024, 'all', 1, 'text')

    def test_xkillKeyHash(self):
        killkey(1024, 1)

    def test_dump(self):
        redisdump()

    def test_autoExpire2(self):
        addhash(1025, {'test': 1}, 2)

    def test_autoExpire11(self):
        addhash(1026, {'test': 1}, 11)

    def test_autoExpire15(self):
        addhash(1027, {'test': 1}, 15)
