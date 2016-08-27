import unittest
exec(open("src/Airport.py").read())

"""
Test functionality of base Airport class
"""
class AirportTestCase(unittest.TestCase):

    def setUp(self):
        self.cityA = Airport('City A', 1, [123, 456])
        self.cityB = Airport('Foobarbaz', 2, [1000, 2345])

    def tearDown(self):
        pass

    def testGetCityName(self):
        assert self.cityA.getCityName() == "City A", "getCityName() returned incorrect string"

    def testGetCityClass(self):
        assert self.cityA.getClass() == 1, "getCityClass() returned incorrect value"

    def testGetLoc(self):
        assert len(self.cityB.getLoc()) == 2, "getLoc() returned list of incorrect size"
        assert self.cityB.getLoc() == [1000, 2345], "getLoc() returned incorrect values"

    def testGetLocX(self):
        assert self.cityA.getLocX() == 123, "getLocX() returned incorrect value"

    def testGetLocY(self):
        assert self.cityB.getLocY() == 2345, "getLocY() returned incorrect value"
