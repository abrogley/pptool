import unittest
exec(open("test/MoreAsserts.py").read())
exec(open("src/RouteManager.py").read())

"""
Test functionality of base Airport class
"""
class RouteManagerTestCase(unittest.TestCase):

    def setUp(self):
        pass      

    def tearDown(self):
        pass

    def testTrivial(self):
        assert 1 == 1