class AirportList(object):
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

    "Find distance between two cities or locations by their names, Airport (py) class, or coordinates"
    def getDistanceBetween(self, firstLoc, secondLoc):
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
        distance = (xDistance**2 + yDistance**2)**0.5
        return distance

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
    Find the list of all airports within range of named airport
    with optional airport class filter.
    """
    def findAirportsWithinRange(self, airportName, rangeDistance, minClass=1):
        subsetWithinRange = []
        for ii in range(len(self.airports)):
            candidateAirport = self.airports[ii]
            
            if airportName is candidateAirport.getCityName():
                continue
            
            if (self.getDistanceBetween(airportName, candidateAirport.getCityName()) < rangeDistance) :
                if candidateAirport.getClass() < minClass :
                    continue
                else :
                    subsetWithinRange.append(candidateAirport)
                
        return subsetWithinRange

    """
    This method finds the best transfer city between two other cities by minimizing total range traveled
    A minimum class may be specified
    A maximum range may be specified
    """
    def findBestMidpointAirport(self, firstLoc, secondLoc, minClass=1, maxRange=100000, desiredType=str):        
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

        if desiredType == str :
            return self.airports[bestIndexSoFar].getCityName()
        elif desiredType == Airport :
            return self.airports[bestIndexSoFar]
