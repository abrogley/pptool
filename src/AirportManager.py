from operator import itemgetter, attrgetter

class AirportManager(object):
    "class with many operations available for the list of airports"
    def __init__(self, inputList):
        self.baseFare             = 50
        self.coinsPerUnitDistance = 0.25

        "Airport coordinates from some input source"
        self.airports = inputList

    "Look up an Airport class instance by city name"
    def findByName(self, searchString):
        for ap in self.airports:
            if searchString == ap.getCityName() :
                return ap
        #print "Could not find city named " + searchString + "."
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
                return -4

        # Similarly, let's encapsulate a single string or single Airport as a list.
        if type(inputs) is Airport or type(inputs) is str:
            inputs = [inputs]

        # By now, everything should be a list. If not, return error.
        if type(inputs) is not list :
            # Type error. List expected
            return -3

        for item in inputs:
            # After this adjustment, inputs is now a list of list(s), string(s), and/or
            # Airport(s). The inputs list need not contain items all of the same type,
            # but each item must be one of these types.
            if type(item) not in [list, str, Airport]:
                # Type error of input item in list
                return -2

            # First, find the Airport by string name if needed
            if type(item) is str :
                item = self.findByName(item)
                if item == "":
                    # Could not find a city by the string name in item
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
        if type(firstLoc) is str :
            firstLoc = self.findByName(firstLoc)
            if firstLoc == "":
                return -1
        if type(firstLoc) is Airport :
            firstLoc = firstLoc.getLoc()
        if type(secondLoc) is str :
            secondLoc = self.findByName(secondLoc)
            if secondLoc == "":
                return -1
        if type(secondLoc) is Airport :
            secondLoc = secondLoc.getLoc()
        xDistance = secondLoc[0] - firstLoc[0]
        yDistance = secondLoc[1] - firstLoc[1]
        return [xDistance, yDistance]

    "Find distance between two cities or locations by their names, Airport (py) class, or coordinates"
    def getDistanceBetween(self, firstLoc, secondLoc):
        distVector = self.findVector(firstLoc, secondLoc)
        distance = (distVector[0]**2 + distVector[1]**2)**0.5
        return distance

    """
    Find the unit vector from first city to second city.
    """
    def findUnitVector(self, firstLoc, secondLoc):
        distVector = self.findVector(firstLoc, secondLoc)
        distance = (distVector[0]**2 + distVector[1]**2)**0.5
        if distance > 0 :
            unitVector = [x/distance for x in distVector]
            return unitVector
        else :
            return [1,0]

    "Find midpoint(s) between two cities"
    def getMidpointBetween(self, firstLoc, secondLoc, numDivisions=2):
        if type(firstLoc) is str :
            firstLoc = self.findByName(firstLoc)
        if type(firstLoc) is Airport :
            firstLoc = firstLoc.getLoc()
        if type(secondLoc) is str :
            secondLoc = self.findByName(secondLoc)
        if type(secondLoc) is Airport :
            secondLoc = secondLoc.getLoc()

        # Simple bisection case
        if numDivisions == 2:
            xMidpoint = (secondLoc[0] + firstLoc[0])/2.0
            yMidpoint = (secondLoc[1] + firstLoc[1])/2.0
            return [xMidpoint, yMidpoint]
        # Generic n-section case
        else:
            weightings = [1.0*x/numDivisions for x in range(1, numDivisions)]
            midpoints = []
            for w in weightings:
                thisPoint = [w*secondLoc[0] + (1.0-w)*firstLoc[0], \
                             w*secondLoc[1] + (1.0-w)*firstLoc[1]]
                midpoints.append(thisPoint)
            return midpoints


    "Find nearest airport to a given x,y coordinate"
    def findNearestAirport(self, firstLoc, minClass=1, desiredType=str):
        if type(firstLoc) is str :
            firstLoc = self.findByName(firstLoc)
        if type(firstLoc) is Airport :
            firstLoc = firstLoc.getLoc()

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
    def costBetween(self, firstLoc, secondLoc):
        cost = self.getDistanceBetween(firstLoc, secondLoc) * self.coinsPerUnitDistance + self.baseFare
        return cost

    """
    This method finds the best transfer city between two other cities by minimizing total distance traveled
    A minimum class may be specified
    A maximum range may be specified

    If no single city is found, then a -1 is returned
    If the two cities are within range of each other, the first Airport alphabetically by city name is returned.
    """
    def findBestTransferAirport(self, firstLoc, secondLoc, minClass=1, maxRange=100000, desiredType=str):
        if type(firstLoc) is str :
            firstLoc = self.findByName(firstLoc)
        if type(firstLoc) is Airport :
            firstLoc = firstLoc.getLoc()

        leastExtraRangeSoFar = 1000000
        bestIndexSoFar = -1

        totalRange = self.getDistanceBetween(firstLoc, secondLoc)

        for ii in range(len(self.airports)):
            if self.airports[ii].getClass() < minClass :
                continue
            else :
                currentRange1 = self.getDistanceBetween(self.airports[ii], firstLoc)
                currentRange2 = self.getDistanceBetween(self.airports[ii], secondLoc)
                if currentRange1 > maxRange or currentRange2 > maxRange :
                    continue

                currentExtraRange = currentRange1 + currentRange2 - totalRange
                if currentExtraRange < leastExtraRangeSoFar :
                    bestIndexSoFar = ii
                    leastExtraRangeSoFar = currentExtraRange

        if bestIndexSoFar == -1 :
            # This means no transfer city was found less than maxRange
            return -1

        if desiredType == str :
            return self.airports[bestIndexSoFar].getCityName()
        elif desiredType == Airport :
            return self.airports[bestIndexSoFar]

    """
    Find the list of all airports within range of named airport
    with optional airport class filter.
    """
    def findAirportsWithinRange(self, airportName, maxRange, minClass=1):
        subsetWithinRange = []
        for ii in range(len(self.airports)):
            candidateAirport = self.airports[ii]

            if airportName is candidateAirport.getCityName():
                continue

            if (self.getDistanceBetween(airportName, candidateAirport.getCityName()) < maxRange) :
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

    """
    This method attempts to find the best route between two points on the map using only
    known Airports as stopovers. It is an implementation of the A* pathfinding algorithm.

    1. A list of cities within range of the starting location are found.

    2. These cities are ranked by their remaining distance to the target city.

    3. The top ranked city is chosen to be the next point to search from

    3. Repeat from Step 1 using the closest city to target

    4. If a path is found, return the list of cities.

    5. If no path is found, try the next best city option from the starting point

    6. If no path is found after exhausting all the options from the first location, start
        checking all options from the best city in Step 2. (NOT YET IMPLEMENTED)

    7. If no path is found after exhausting all intermediate cities, return -1 for no path found
    """
    def findARouteBetween(self, firstLoc, secondLoc, minClass=1, maxRange=100000):
        # Steps 1-4
        maxSteps = 20
        pathway = [firstLoc]
        for ii in range(maxSteps):
            citiesToCheck = self.findAirportsTowards(pathway[-1], secondLoc, maxRange, minClass)
            if len(citiesToCheck) > 0 :
                jj = 0
                inWhileLoop = True
                while inWhileLoop :
                    #Don't add a city already in our pathway.
                    if citiesToCheck[jj] not in pathway :
                        pathway.append(citiesToCheck[jj])
                        inWhileLoop = False
                    else :
                        if jj >= len(citiesToCheck):
                            inWhileLoop = False
                            continue
                        jj += 1

                #If we hit our target destination, we're done.
                if citiesToCheck[jj] == secondLoc :
                    break
        return pathway

    """
    Iterate on this path by seeing if there is range savings anywhere.
    """
    def improveRoute(self, pathway, minClass=1, maxRange=100000):
        debugOn = False
        # Compare three consecutive cities in the pathway to see if another intermediate
        # city results in a shorter path.
        pathLength = len(pathway)
        previousPathway = list(pathway)
        inWhileLoop = True
        jj = 0
        while inWhileLoop :
            inWhileLoop = False
            ii = 0
            while ii < pathLength-2 :
                airportN      = pathway[ii]
                airportNplus1 = pathway[ii+1]
                airportNplus2 = pathway[ii+2]
                betterNplus1 = self.findBestTransferAirport(airportN, airportNplus2, minClass, maxRange, Airport)
                if airportNplus1 is not betterNplus1 :
                    if debugOn:
                       print "      Found a better route!"
                       print "         instead of " + airportN.getCityName() + "->" + airportNplus1.getCityName() + "->" + airportNplus2.getCityName()
                       print "         there is " + airportN.getCityName() + "->" + betterNplus1.getCityName() + "->" + airportNplus2.getCityName()
                    pathway[ii+1] = betterNplus1
                ii += 1

            for kk in range(len(previousPathway)) :
                if previousPathway[kk].getCityName() is not pathway[kk].getCityName() :
                    extraText =  "         These are different!"
                    inWhileLoop = True
                else :
                    extraText = ""
                    inWhileLoop = False or inWhileLoop
                if debugOn:
                    print "      " + previousPathway[kk].getCityName() + "     " + pathway[kk].getCityName() + extraText

            previousPathway = list(pathway)
            jj += 1
            if not inWhileLoop and debugOn:
                print "  Converged after " + str(jj) + " iterations."

        # Remove duplicates before returning value
        pathway = self.removeDuplicates(pathway)
        return pathway

    """
    Remove duplicate cities from pathway.
    """
    def removeDuplicates(self, pathway):
        # Remove duplicate cities from list, iff they are adjacent. (They should never not be adjacent)
        # Start from the end of the list to avoid indexing errors
        pathLength = len(pathway)
        for ii in range(pathLength-1,0,-1):
            if pathway[ii] == pathway[ii-1]:
                del pathway[ii]
        return pathway

    """
    It's possible that in the pathway found thus far, one transfer city would be better replaced
    by two transfer cities. An example would be Bogota to Barcelona using class 2+ cities on a
    fully upgraded Aeroeagle. The shortest 1-transfer route is through Recife, while the shortest
    overall route is through Caracas and Madrid.
    """
    def tryAdditionalTransferCities(self, pathway, minClass=1, maxRange=100000):
        # The path length will increase during this method, so grab initial length.
        pathLength = len(pathway)

        # Start from the end of the list to avoid indexing errors
        for ii in range(pathLength-2, 0, -1):
            # Get new midpoints between ii-1 and ii+1
            midpoints = self.getMidpointBetween(pathway[ii-1], pathway[ii+1], 6)

            # Find closest cities to these midpoints
            midpointAirports = []
            for mp in midpoints:
                midpointAirports.append(airports.findNearestAirport(mp, minClass, Airport))

            # Replace the city ii with these midpoint cities
            pathway = pathway[:ii] + midpointAirports + pathway[ii+1:]

        # Remove duplicates, if any.
        pathway = self.removeDuplicates(pathway)
        return pathway

    """
    Combination of the above algorithms to get the best route.
    """
    def findBestRouteBetween(self, firstLoc, secondLoc, minClass=1, maxRange=100000):
        # First get a viable path given range and class constraints.
        pathway = self.findARouteBetween(firstLoc, secondLoc, minClass, maxRange)

        # Throw in more intermediate cities
        if len(pathway) > 2:
            pathway = self.tryAdditionalTransferCities(pathway, minClass, maxRange)
            pathway = self.improveRoute(pathway, minClass, maxRange)

        # Then improve the path, FIXME for some routes this must be done more than once, e.g. Honolulu to Easter Island on a Mohawk
        if len(pathway) > 2:
            for ii in range(3):
                pathway = self.improveRoute(pathway, minClass, maxRange)

        # if len(pathway) is 2, it is a nonstop route
        # if len(pathway) is 1, then there was no route found.
        return pathway

