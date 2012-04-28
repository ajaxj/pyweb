# -*- coding:utf-8 -*-
# unit test
from couch_test1 import CouchTests2

__author__ = 'Administrator'

import unittest

class CouchTests(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(1,1)

    def test_bar(self):
        self.assertEqual(1,1)







def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CouchTests2, 'test'))
    suite.addTest(unittest.makeSuite(CouchTests, 'test'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')

