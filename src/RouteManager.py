from operator import itemgetter, attrgetter

class RouteManager(object):
    "class with many operations available for the list of airports"
    def __init__(self, airportManager):
        "Airport manager from some input source"
        self.am = airportManager

    """
    This method finds the best transfer city between two other cities by minimizing total distance traveled
    A minimum class may be specified
    A maximum range may be specified

    If no single city is found, then a -1 is returned
    If the two cities are within range of each other, the first Airport alphabetically by city name is returned.
    """
    def findBestTransferAirport(self, firstLoc, secondLoc, minClass=1, maxRange=100000, desiredType=str):
        locList = self.am.parseInputs([firstLoc, secondLoc])
        if type(locList) is int:
            return locList
        firstLoc = locList[0]
        secondLoc = locList[1]

        leastExtraRangeSoFar = 1000000
        bestIndexSoFar = -5

        totalRange = self.am.getDistanceBetween(firstLoc, secondLoc)

        for ii in range(len(self.am.airports)):
            if self.am.airports[ii].getClass() < minClass :
                continue
            else :
                currentRange1 = self.am.getDistanceBetween(self.am.airports[ii], firstLoc)
                currentRange2 = self.am.getDistanceBetween(self.am.airports[ii], secondLoc)
                if currentRange1 > maxRange or currentRange2 > maxRange :
                    continue

                currentExtraRange = currentRange1 + currentRange2 - totalRange
                if currentExtraRange < leastExtraRangeSoFar :
                    bestIndexSoFar = ii
                    leastExtraRangeSoFar = currentExtraRange

        if bestIndexSoFar < 0 :
            # This means no transfer city was found less than maxRange
            return bestIndexSoFar

        if desiredType == str :
            return self.am.airports[bestIndexSoFar].getCityName()
        elif desiredType == Airport :
            return self.am.airports[bestIndexSoFar]

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
            citiesToCheck = self.am.findAirportsTowards(pathway[-1], secondLoc, maxRange, minClass)
            if len(citiesToCheck) > 0 :
                jj = 0
                inWhileLoop = True
                while inWhileLoop :
                    #Don't add a city already in our pathway.
                    if citiesToCheck[jj] not in pathway :
                        pathway.append(citiesToCheck[jj])
                        inWhileLoop = False
                    else :
                        if jj >= len(citiesToCheck) - 1:
                            inWhileLoop = False
                            return -6
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
                       print( "      Found a better route!" )
                       print( "         instead of " + airportN.getCityName() + "->" + airportNplus1.getCityName() + "->" + airportNplus2.getCityName() )
                       print( "         there is " + airportN.getCityName() + "->" + betterNplus1.getCityName() + "->" + airportNplus2.getCityName() )
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
                    print( "      " + previousPathway[kk].getCityName() + "     " + pathway[kk].getCityName() + extraText )

            previousPathway = list(pathway)
            jj += 1
            if not inWhileLoop and debugOn:
                print( "  Converged after " + str(jj) + " iterations." )

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
        #for cc in pathway:
        #    print( cc.getCityName() )

        # Start from the end of the list to avoid indexing errors
        for ii in range(pathLength-2, 0, -1):
            # Get new midpoints between ii-1 and ii+1
            distance = self.am.getDistanceBetween(pathway[ii-1], pathway[ii+1])
            # FIXME: 4 midpoints is needed for severe cases like Honolulu to Easter Island
            midpoints = self.am.getMidpointBetween(pathway[ii-1], pathway[ii+1], 4)
            for mp in midpoints :
                if type(mp) is int :
                    print( "ERROR: Problem in finding midpoints" )
                    
            # Find closest cities to these midpoints
            midpointAirports = []
            for mp in midpoints:
                nearestToMp = self.am.findNearestAirport([mp], minClass, Airport)
                if nearestToMp is not int :
                    midpointAirports.append(nearestToMp)
            # Remove city ii and insert midpoing list between the city ii and ii+1
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
        
        if type(pathway) is int :
            return []
        
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

