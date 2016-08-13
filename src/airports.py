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
        foundAirport = -1
        for ii in range(len(self.airports)):
            if searchString is self.airports[ii].getCityName() :
                foundAirport = ii
        if foundAirport < 0 :
            print "Could not find city named " + searchString + "."
            return -1
        else :
            return self.airports[foundAirport]

    """
    Find the vector from first city to second city.
    """
    def findVector(self, firstLoc, secondLoc):
        if type(firstLoc) is str :
            firstLoc = self.findByName(firstLoc)
        if type(firstLoc) is Airport :
            firstLoc = firstLoc.getLoc()
        if type(secondLoc) is str :
            secondLoc = self.findByName(secondLoc)
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

    "Find midpoint between two cities by their names"
    def getMidpointBetween(self, firstLoc, secondLoc):
        if type(firstLoc) is str :
            firstLoc = self.findByName(firstLoc)
        if type(firstLoc) is Airport :
            firstLoc = firstLoc.getLoc()
        if type(secondLoc) is str :
            secondLoc = self.findByName(secondLoc)
        if type(secondLoc) is Airport :
            secondLoc = secondLoc.getLoc()
        xMidpoint = (secondLoc[0] + firstLoc[0])/2.0
        yMidpoint = (secondLoc[1] + firstLoc[1])/2.0
        return [xMidpoint, yMidpoint]

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
    
    5. Iterate on this path by seeing if there is range savings anywhere.

    6. If no path is found, try the next best city option from the starting point

    7. If no path is found after exhausting all the options from the first location, start
        checking all options from the best city in Step 2.

    8. If no path is found after exhausting all intermediate cities, return -1 for no path found
    """
    def findBestRouteBetween(self, firstLoc, secondLoc, minClass=1, maxRange=100000, desiredType=str):
        # Steps 1-4
        maxSteps = 20
        pathway = [firstLoc]
        for ii in range(maxSteps):
            citiesToCheck = self.findAirportsTowards(pathway[-1], secondLoc, maxRange, minClass)
            if len(citiesToCheck) > 1 :
                if citiesToCheck[0] not in pathway :
                    pathway.append(citiesToCheck[0])
                else :
                    pathway.append(citiesToCheck[1])
                if citiesToCheck[0] == secondLoc :
                    break
        
        # Step 5
        pathLength = len(pathway)
        initPathway = pathway
        inWhileLoop = True
        while inWhileLoop :
            ii = 0
            while ii < pathLength-2 :
                airportN      = pathway[ii]
                airportNplus1 = pathway[ii+1]
                airportNplus2 = pathway[ii+2]
                betterNplus1 = self.findBestTransferAirport(airportN, airportNplus2, minClass, maxRange, Airport)
                if airportNplus1 is not betterNplus1 :
                    pathway[ii+1] = betterNplus1
                ii += 1
            if pathway is initPathway:
                inWhileLoop = False

        for ii in range(pathLength-1,0,-1):
            if pathway[ii] == pathway[ii-1]:
                del pathway[ii]
        
        return pathway
