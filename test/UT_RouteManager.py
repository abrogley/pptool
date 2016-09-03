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

        self.mohawkPairs = [
            [20,188],
            [0,1],
            [2,3],
            [4,5],
            [6,7],
            [8,7],
            [34,50],
            [162,240],
            [90,71],
            ]
        
        # These are the efficiencies for each of the routes. Better results
        # may technically be possible. These values ensure no regressions.
        self.mohawkPairEfficiencies = [
            0.9655751926,
            0.9533862207,
            0.9977849223,
            0.9920216103,
            0.9268054996,
            0.8939525271,
            0.5239262268,
            0.9266858049,
            0.4942720188,
            ]
        
        self.aeroeaglePairs = [
            [32,18],
            [90,219],
            [84,204],
            [156,67],
            ]
        
        self.aeroeaglePairEfficiencies = [
            0.9940510257,
            0.9816157295,
            0.9984755279,
            0.9259455952,
            ]
        

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
        
    def testRemoveDuplicates(self):
        self.pathway = [self.newYork, self.newYork, self.cairo, self.cairo, self.cairo,
                        self.newYork, self.newYork, self.newYork, self.newYork]
        shortPathway = self.rm.removeDuplicates(self.pathway)
        assert shortPathway == [self.newYork, self.cairo, self.newYork]
        
    def testFindBestPathwayMohawk(self):
        pairIter = 0
        for p in self.mohawkPairs:
            cumRange = 0
            ii = 0
            bestRoute = self.rm.findBestRouteBetween(self.ad[p[0]], self.ad[p[1]], 1, 1150)
            for sr in bestRoute :
                if ii > 0:
                    cumRange += self.am.getDistanceBetween(bestRoute[ii-1], bestRoute[ii])
                ii += 1
            perfectRange = self.am.getDistanceBetween(bestRoute[0], bestRoute[-1])
            routeEfficiency = perfectRange/cumRange
            assert routeEfficiency >= self.mohawkPairEfficiencies[pairIter]
            pairIter += 1
            
    def testFindBestPathwayAeroeagle(self):
        pairIter = 0
        for p in self.aeroeaglePairs:
            cumRange = 0
            ii = 0
            bestRoute = self.rm.findBestRouteBetween(self.ad[p[0]], self.ad[p[1]], 2, 2300)
            for sr in bestRoute :
                if ii > 0:
                    cumRange += self.am.getDistanceBetween(bestRoute[ii-1], bestRoute[ii])
                ii += 1
            perfectRange = self.am.getDistanceBetween(bestRoute[0], bestRoute[-1])
            routeEfficiency = perfectRange/cumRange
            assert routeEfficiency >= self.aeroeaglePairEfficiencies[pairIter]
            pairIter += 1
        