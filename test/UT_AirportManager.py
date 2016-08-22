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
        self.singleLoc = [123, 456]
        self.singleLocInNestedList = [[234, 567]]
        self.volgograd = self.am.findByName('Volgograd')
        self.houston = self.am.findByName('Houston')
        self.saoPaolo = self.am.findByName('Sao Paolo')
        self.fakeCity = self.am.findByName('Not a Real City')

    def tearDown(self):
        pass

    def testFindByName(self):
        assert self.houston.getCityName() == "Houston", "findByName() could not find 1 word city"
        assert self.houston.getCityName() != "WRONG NAME", "findByName() found a false positive"
        assert self.saoPaolo.getCityName() == "Sao Paolo", "findByName() could not find 2 word city"
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
        badfind = self.am.findVector('Houston','Not a Real City')
        assert badfind == -1

