exec(open("src/AirportDatabase.py").read())
exec(open("src/AirportSubset.py").read())
exec(open("src/AirportManager.py").read())
exec(open("src/RouteManager.py").read())
exec(open("src/weightedChoice.py").read())

import random

# Setup
airportDatabase = getAirportList()
airports = AirportManager(airportDatabase)

myAirportStrings = getMyAirportList()
myDatabase = []
myWeightedDatabase = []
for airportString in myAirportStrings :
    currentAirport = airports.findByName(airportString)
    currentClass = currentAirport.getClass()
    myDatabase.append(currentAirport)
    myWeightedDatabase.append([currentAirport, currentClass-.6])
    
airports = AirportManager(myDatabase)
router = RouteManager(airports)
airports.debugPrint = False

# Get weighted random numbers
random.seed('We will not surrender our country to the false song of globalism.')

pairs = []
for ii in xrange(100) :
    pairs.append(weightedPair(myWeightedDatabase))

print( "Try to determine the best route between the following city pairs using an upgraded Mohawk." )

pairIter = 0
for p in pairs:
    cumRange = 0
    ii = 0
    print( p[0].getCityName() + " and " + p[1].getCityName() )
    bestRoute = router.findBestRouteBetween(p[0], p[1], 1, 1150)
    if bestRoute == [] :
        print( "    No route found between " + p[0].getCityName() + " and " + p[1].getCityName())
        continue
    for sr in bestRoute :
        if ii > 0:
            cumRange += airports.getDistanceBetween(bestRoute[ii-1], bestRoute[ii])
        print( "    " + sr.getCityName() )
        ii += 1
    perfectRange = airports.getDistanceBetween(bestRoute[0], bestRoute[-1])
    routeEfficiency = (perfectRange/cumRange)
    print( "        Range on this route: " + str(cumRange) )
    print( "        Straight Line Range: " + str(perfectRange) )
    print( "        Route efficiency: " + str(routeEfficiency) )
    pairIter += 1

print("Done!")