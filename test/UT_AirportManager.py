import unittest
execfile("src/AirportManager.py")
execfile("src/AirportDatabase.py")

"""
Test functionality of base Airport class
"""
class AirportManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.ad = getAirportList() #load Airport Database
        self.am = AirportManager(self.ad)
        self.houston = self.am.findByName('Houston')
        self.saoPaolo = self.am.findByName('Sao Paolo')

    def tearDown(self):
        pass

    def testFindByName(self):
        self.fakeCity = self.am.findByName('Not a Real City')
        assert self.houston.getCityName() == "Houston", "findByName() could not find 1 word city"
        assert self.houston.getCityName() != "WRONG NAME", "findByName() found a false positive"
        assert self.saoPaolo.getCityName() == "Sao Paolo", "findByName() could not find 2 word city"
        assert self.fakeCity == "", "findByName() found a city not in the list"

    def testFindVector(self):
        vec1 = self.am.findVector('Houston','Sao Paolo')
        assert vec1 == [1436, 1648]
        vec2 = self.am.findVector([1234, 5678], [2345, 3456])
        assert vec2 == [1111, -2222]
        vec3 = self.am.findVector(self.ad[4], self.ad[5]) #Algiers to Alice Springs
        assert vec3 == [3956, 1936]
        

if __name__ == "__main__":
    unittest.main() # run all tests
