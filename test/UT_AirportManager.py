import unittest
exec(open("test/MoreAsserts.py").read())
exec(open("src/AirportManager.py").read())
exec(open("src/AirportDatabase.py").read())

"""
Test functionality of base Airport class
"""
class AirportManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.ad = getAirportList() #load Airport Database
        self.am = AirportManager(self.ad)
        self.am.debugPrint = False
        self.singleLoc = [123, 456]
        self.singleLocInNestedList = [[234, 567]]
        self.volgograd = self.am.findByName('Volgograd')
        self.houston = self.am.findByName('Houston')
        self.saoPaolo = self.am.findByName('Sao Paolo')
        self.fakeCity = self.am.findByName('Not a Real City')
        self.xian = self.am.findByName('Xi\'an')
        self.stPete = self.am.findByName('St. Petersburg')          

    def tearDown(self):
        pass

    def testFindByName(self):
        assert self.houston.getCityName() == "Houston", "findByName() could not find 1 word city"
        assert self.houston.getCityName() != "WRONG NAME", "findByName() found a false positive"
        assert self.saoPaolo.getCityName() == "Sao Paolo", "findByName() could not find 2 word city"
        assert self.xian.getCityName() == "Xi\'an", \
               "findByName() could not find Xi'an. Problem with apostrophe?"
        assert self.stPete.getCityName() == "St. Petersburg", \
               "findByName() could not find St. Petersburg. Problem with period?"
        assert self.fakeCity == "", "findByName() found a city not in the list"

    def testParseInputsPassThru(self):
        # Make sure the passthrough of a single location works
        passThruSingleLoc = self.am.parseInputs(self.singleLoc)
        assert passThruSingleLoc == [self.singleLoc]
        passThruSingleLocInNestedList = self.am.parseInputs(self.singleLocInNestedList)
        assert passThruSingleLocInNestedList == self.singleLocInNestedList

        # Make sure the passthrough of multiple location pairs works
        threeLocs = [[123,456],[-345,678],[567,-890]]
        passThruThreeLocs = self.am.parseInputs(threeLocs)
        assert passThruThreeLocs == threeLocs

    def testParseInputsBadInputInts(self):
        # Make sure integer and list of single int/more than 3 ints do not work
        badInt = self.am.parseInputs(1234)
        assert badInt == -3
        badIntListSingleInt = self.am.parseInputs([333])
        assert badIntListSingleInt == -2
        badIntListMultipleInts = self.am.parseInputs([1555, -5333, 308])
        assert badIntListMultipleInts == -2
        weirdInputs = self.am.parseInputs([555, -333, [5, 15]])
        assert weirdInputs == -2
        badEmptyList = self.am.parseInputs([])
        assert badEmptyList == -4
        badEmptyString = self.am.parseInputs("")
        assert badEmptyString == -1

    def testParseInputsAirports(self):
        # Make sure an Airport not encapsulated in a list is handled properly
        assert self.am.parseInputs(self.houston) == [[2812,4272]]
        # Make sure an Airport encapsulated in a list is handled properly
        assert self.am.parseInputs([self.volgograd]) == [[6984,3488]]
        # Make sure that a list of several Airports is handled properly
        threeAirports = self.am.parseInputs([self.volgograd, self.houston, self.saoPaolo])
        assert threeAirports == [[6984,3488], [2812,4272], [4248,5920]]

    def testParseInputsStrings(self):
        # Make sure an unencapsulated string is handled properly
        assert self.am.parseInputs('Sao Paolo') == [[4248,5920]]
        # Make sure an encapsulated string is handled properly
        assert self.am.parseInputs(['Houston']) == [[2812,4272]]
        # Make sure that a list of several strings is handled properly
        threeStrings = self.am.parseInputs(['Volgograd', 'Houston', 'Sao Paolo'])
        assert threeStrings == [[6984,3488], [2812,4272], [4248,5920]]

    def testParseInputsMultipleTypes(self):
        variousInputs = self.am.parseInputs(['Volgograd', self.houston, [12345, -98765]])
        assert variousInputs == [[6984,3488], [2812,4272], [12345, -98765]]

    def testFindVector(self):
        vec1 = self.am.findVector('Houston','Sao Paolo')
        assert vec1 == [1436, 1648]
        
        vec2 = self.am.findVector([1234, 5678], [2345, 3456])
        assert vec2 == [1111, -2222]
        
        vec3 = self.am.findVector(self.ad[4], self.ad[5]) #Algiers to Alice Springs
        assert vec3 == [3956, 1936]

    def testFindUnitVector(self):
        vec1 = self.am.findUnitVector('Houston','Sao Paolo')
        assertVectorNear( vec1, [0.6569486, 0.7539354] )
        
        vec2 = self.am.findUnitVector([1234, 5678], [2345, 3456])
        assertVectorNear( vec2, [0.4472136, -0.8944272] )
        
        vec3 = self.am.findUnitVector(self.ad[4], self.ad[5]) #Algiers to Alice Springs
        assertVectorNear( vec3, [0.8982091, 0.4395685] )

    def testGetDistanceBetween(self):
        dist1 = self.am.getDistanceBetween('Houston','Sao Paolo')
        assertNear(dist1, 2185.8636737)
        
        dist2 = self.am.getDistanceBetween([1120, 950], [1000, 1000])
        assert dist2 == 130
        
        dist3 = self.am.getDistanceBetween(self.ad[4], self.ad[5]) #Algiers to Alice Springs
        assertNear(dist3, 4404.3196978)

    def testGetMidpointBetween(self):
        mp1 = self.am.getMidpointBetween('Houston','Sao Paolo')
        assertVectorNear(mp1[0], [3530, 5096])

        mp2 = self.am.getMidpointBetween('Houston','Sao Paolo',5)
        assertVectorNear(mp2[0], [3099.2, 4601.6])
        assertVectorNear(mp2[1], [3386.4, 4931.2])
        assertVectorNear(mp2[2], [3673.6, 5260.8])
        assertVectorNear(mp2[3], [3960.8, 5590.4])

    def testFindNearestAirport(self):
        point = [7000,5000]
        na1 = self.am.findNearestAirport(point)
        na2 = self.am.findNearestAirport(point,2)
        na3 = self.am.findNearestAirport(point,3,Airport)
        assert na1 == 'Mogadishu'
        assert na2 == 'Nairobi'
        assert na3.getCityName() == 'Cairo'
        
    def testGetCostBetween(self):
        cost1 = self.am.getCostBetween([1000,0],[2000,0])
        assert cost1 == 300
        cost2 = self.am.getCostBetween('Atlanta','Shenyang')
        assert cost2 == 1606
        cost3 = self.am.getCostBetween('Lagos',self.xian)
        assert cost3 == 877
        
    def testFindAirportsWithinRange(self):
        # Situation with 1 city in range
        list1 = self.am.findAirportsWithinRange(self.houston, 500, 3)
        assert list1[0].getCityName() == 'Mexico City'
        assert len(list1) == 1
        
        #Situation with several cities in range
        list2 = self.am.findAirportsWithinRange('Riga', 500, 2)
        assert len(list2) == 3
        
        #Situation with no cities in range
        list3 = self.am.findAirportsWithinRange([0,0], 800)
        assert len(list3) == 0
        
    def testFindAirportsTowards(self):
        sortedList1 = self.am.findAirportsTowards(self.houston, 'Yellowknife', 400)
        assert sortedList1[0].getCityName() == 'Kansas City'
        assert sortedList1[-1].getCityName() == 'Oaxaca'
        assert len(sortedList1) == 11
        
        sortedList2 = self.am.findAirportsTowards(self.houston, 'Yellowknife', 500, 2)
        assert sortedList2[0].getCityName() == 'Phoenix'
        assert sortedList2[-1].getCityName() == 'Guatemala'
        assert len(sortedList2) == 8
        
        sortedList3 = self.am.findAirportsTowards('Yellowknife', self.houston, 600)
        assert sortedList3[0].getCityName() == 'Saskatoon'
        assert sortedList3[-1].getCityName() == 'Yellowknife'
        assert len(sortedList3) == 4