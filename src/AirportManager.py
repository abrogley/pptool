from operator import itemgetter, attrgetter

class AirportManager(object):
    "class with many operations available for the list of airports"
    def __init__(self, inputList):
        self.baseFare             = 50
        self.coinsPerUnitDistance = 0.25
        self.debugPrint           = True

        "Airport coordinates from some input source"
        self.airports = inputList

    "Look up an Airport class instance by city name"
    def findByName(self, searchString):
        for ap in self.airports:
            if searchString == ap.getCityName() :
                return ap
        #print( "Could not find city named " + searchString + "." )
        return ""

    """
    Inputs may come from various formats and many different methods have a
    need for checking that these various forms are parsed correctly. 'inputs'
    is a list of various elements of possibly different types. Each input item
    in 'inputs' may be:

        - Airport type
        - String
        - List of two integers [a,b]

    These forms will all be reduced down to:
        - List of two integers [a,b]

    The output is a list of these two-length integer pairs.
    """
    def parseInputs(self, inputs):
        returnList = []

        # The only valid input types are list, string, and Airport class.

        # It is possible that an input 'list' happens to be a list of 2 integers,
        # making it just one input location of x and y coordinates. This is a
        # valid input. The following checks for this case and transforms such a
        # list into a list of the original integer pair. [[x, y]] instead of [x,y]
        if type(inputs) is list:
            if len(inputs) == 2:
                if type(inputs[0]) is int and type(inputs[1]) is int:
                    inputs = [inputs]
            elif len(inputs) == 0:
                # There needs to be some kind of input in the list
                if self.debugPrint:
                    print( inputs )
                return -4

        # Similarly, let's encapsulate a single string or single Airport as a list.
        if type(inputs) is Airport or type(inputs) is str:
            inputs = [inputs]

        # By now, everything should be a list. If not, return error.
        if type(inputs) is not list :
            # Type error. List expected
            if self.debugPrint:
                print( inputs )
            return -3

        for item in inputs:
            # After this adjustment, inputs is now a list of list(s), string(s), and/or
            # Airport(s). The inputs list need not contain items all of the same type,
            # but each item must be one of these types.
            if type(item) not in [list, str, Airport]:
                # Type error of input item in list
                if self.debugPrint:
                    print( inputs )
                return -2

            # First, find the Airport by string name if needed
            if type(item) is str :
                item = self.findByName(item)
                if item == "":
                    # Could not find a city by the string name in item
                    if self.debugPrint:
                        print( inputs )
                    return -1

            # Then, get the location of the Airport.
            if type(item) is Airport :
                item = item.getLoc()

            # By this point, an input item of any valid type should have been
            # reduced to a list of two integers. Append that to the return list
            returnList.append(item)

        return returnList

    """
    Find the vector from first city to second city.
    """
    def findVector(self, firstLoc, secondLoc):
        locList = self.parseInputs([firstLoc, secondLoc])
        if type(locList) is int:
            return locList
        firstLoc = locList[0]
        secondLoc = locList[1]
        
        xDistance = secondLoc[0] - firstLoc[0]
        yDistance = secondLoc[1] - firstLoc[1]
        return [xDistance, yDistance]

    """
    Find distance between two cities or locations by their names, Airport (type),
    or coordinates
    """
    def getDistanceBetween(self, firstLoc, secondLoc):
        locList = self.parseInputs([firstLoc, secondLoc])
        if type(locList) is int:
            return locList
        firstLoc = locList[0]
        secondLoc = locList[1]
        
        distVector = self.findVector(firstLoc, secondLoc)
        distance = (distVector[0]**2 + distVector[1]**2)**0.5
        return distance

    """
    Find the unit vector from first city to second city.
    """
    def findUnitVector(self, firstLoc, secondLoc):
        locList = self.parseInputs([firstLoc, secondLoc])
        if type(locList) is int:
            return locList
        firstLoc = locList[0]
        secondLoc = locList[1]
        
        distVector = self.findVector(firstLoc, secondLoc)
        distance = self.getDistanceBetween(firstLoc, secondLoc)
        if distance > 0 :
            unitVector = [x/distance for x in distVector]
            return unitVector
        else :
            return [1,0]

    "Find midpoint(s) between two cities"
    def getMidpointBetween(self, firstLoc, secondLoc, numDivisions=2):
        locList = self.parseInputs([firstLoc, secondLoc])
        if type(locList) is int:
            print( "firstLoc is of type " + type(firstLoc) )
            print( "secondLoc is of type " + type(secondLoc) )
            return locList
        firstLoc = locList[0]
        secondLoc = locList[1]

        weightings = [1.0*x/numDivisions for x in range(1, numDivisions)]
        midpoints = []
        for w in weightings:
            thisPoint = [w*secondLoc[0] + (1.0-w)*firstLoc[0], \
                         w*secondLoc[1] + (1.0-w)*firstLoc[1]]
            midpoints.append(thisPoint)
        return midpoints


    "Find nearest airport to a given x,y coordinate"
    def findNearestAirport(self, firstLoc, minClass=1, desiredType=str):
        locList = self.parseInputs(firstLoc)
        if type(locList) is int:
            # Int is only returned upon not parsing inputs properly
            return locList
        firstLoc = locList[0]

        bestRangeSoFar = 1000000
        bestIndexSoFar = -1

        for ii in range(len(self.airports)):
            if self.airports[ii].getClass() < minClass :
                continue
            else :
                currentRange = self.getDistanceBetween(self.airports[ii], firstLoc)
                if currentRange < bestRangeSoFar :
                    bestIndexSoFar = ii
                    bestRangeSoFar = currentRange

        if desiredType == str :
            return self.airports[bestIndexSoFar].getCityName()
        elif desiredType == Airport :
            return self.airports[bestIndexSoFar]


    "Find the job cost (payout) between two cities by their names"
    def getCostBetween(self, firstLoc, secondLoc):
        locList = self.parseInputs([firstLoc, secondLoc])
        if type(locList) is int:
            return locList
        firstLoc = locList[0]
        secondLoc = locList[1]
        
        cost = int(self.getDistanceBetween(firstLoc, secondLoc) * self.coinsPerUnitDistance + self.baseFare)
        return cost

    """
    Find the list of all airports within range of named airport
    with optional airport class filter.
    """
    def findAirportsWithinRange(self, firstLoc, maxRange, minClass=1):
        locList = self.parseInputs([firstLoc])
        if type(locList) is int:
            return locList
        firstLoc = locList[0]
        
        subsetWithinRange = []
        for ii in range(len(self.airports)):
            candidateAirport = self.airports[ii]

            if firstLoc is candidateAirport.getCityName():
                continue

            if (self.getDistanceBetween(firstLoc, candidateAirport.getCityName()) < maxRange) :
                if candidateAirport.getClass() < minClass :
                    continue
                else :
                    subsetWithinRange.append(candidateAirport)

        return subsetWithinRange

    """
    Similar to findAirportsWithinRange, this returns all airports within a given range,
    but then sorts them based on their remaining distance to the target city
    """
    def findAirportsTowards(self, firstLoc, secondLoc, maxRange, minClass=1):
        airportsNearFirstLoc = self.findAirportsWithinRange(firstLoc, maxRange, minClass)
        numAirportsFound = len(airportsNearFirstLoc)
        distanceAirportPair = []
        for ap in airportsNearFirstLoc:
            distanceAirportPair.append((ap, self.getDistanceBetween(ap, secondLoc)))
        #Do the sort
        sortedAirportPairs = sorted(distanceAirportPair, key=itemgetter(1))
        #Remove distances from tuple
        sortedAirports = []
        for sap in sortedAirportPairs:
            sortedAirports.append(sap[0])
        return sortedAirports