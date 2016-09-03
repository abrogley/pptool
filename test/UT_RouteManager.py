import unittest
exec(open("test/MoreAsserts.py").read())
exec(open("src/RouteManager.py").read())

"""
Test functionality of base Airport class
"""
class RouteManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.ad = getAirportList() #load Airport Database
        self.am = AirportManager(self.ad)
        self.rm = RouteManager(self.am)
        self.am.debugPrint = False
        self.newYork = self.am.findByName('New York')
        self.cairo = self.am.findByName('Cairo')
        self.dist = self.am.getDistanceBetween(self.newYork,self.cairo)

    def tearDown(self):
        pass

    def testFindBestTransferIdeal(self):
        # Find best transfer city with a range constraint of 99% of original distance between cities.
        
        # Class 1 airplane
        best1 = self.rm.findBestTransferAirport(self.newYork, self.cairo, 1, 0.99*self.dist, Airport)
        assert best1.getCityName() == 'Casablanca'
        
        # Class 2 airplane
        best2 = self.rm.findBestTransferAirport(self.newYork, self.cairo, 2, 0.99*self.dist, Airport)
        assert best2.getCityName() == 'Algiers'
        
        # Class 3 airplane
        best3 = self.rm.findBestTransferAirport(self.newYork, self.cairo, 3, 0.99*self.dist, Airport)
        assert best3.getCityName() == 'Paris'


    def testFindBestTransferWithActualAircraft(self):
        # Find best single transfer city using actual in-game airplanes.
        
        # Fully upgraded Mohawk, range = 1150
        bestReal1 = self.rm.findBestTransferAirport(self.newYork, self.cairo, 1, 1150, Airport)
        assert bestReal1 < 0
        
        # Fully upgraded Aeroeagle, range = 2300
        bestReal2 = self.rm.findBestTransferAirport(self.newYork, self.cairo, 2, 2300, Airport)
        assert bestReal2.getCityName() == 'Madrid'
        
        # Fully upgraded Cloudliner, range = 3576
        bestReal3 = self.rm.findBestTransferAirport(self.newYork, self.cairo, 3, 3576, Airport)
        assert bestReal3.getCityName() == 'Cairo' or bestReal3.getCityName() == 'New York'