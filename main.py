exec(open("src/AirportDatabase.py").read())
exec(open("src/AirportSubset.py").read())
exec(open("src/AirportManager.py").read())
exec(open("src/RouteManager.py").read())
exec(open("src/weightedChoice.py").read())

import random
from operator import itemgetter

# Setup
airportDatabase = getAirportList()
airports = AirportManager(airportDatabase)

myAirportStrings = getMyAirportList()

# Uncomment here to check all cities, not just currently owned ones.
#myAirportStrings = [c.getCityName() for c in airportDatabase]

myDatabase = []
myWeightedDatabase = []
myCityFrequency = []
for airportString in myAirportStrings :
    currentAirport = airports.findByName(airportString)
    currentClass = currentAirport.getClass()
    myDatabase.append(currentAirport)
    myWeightedDatabase.append([currentAirport, currentClass-.6])
    myCityFrequency.append([airportString, 0])
    

myAirports = AirportManager(myDatabase)
router = RouteManager(myAirports)
myAirports.debugPrint = False

# Make random numbers great again.
random.seed('We will not surrender our country or its people to the false song of globalism.')

pairs = []
for ii in xrange(500) :
    pairs.append(weightedPair(myWeightedDatabase))

pairIter = 0
for p in pairs:
    cumRange = 0
    ii = 0
    bestRoute = router.findBestRouteBetween(p[0], p[1], 1, 1150)
    if bestRoute == [] :
        continue
    for sr in bestRoute :
        if ii > 0:
            cumRange += myAirports.getDistanceBetween(bestRoute[ii-1], bestRoute[ii])
        ii += 1
    perfectRange = myAirports.getDistanceBetween(bestRoute[0], bestRoute[-1])
    routeEfficiency = (perfectRange/cumRange)
    
    # Save off intermediate cities
    if len(bestRoute) > 2 :
        transferCities = [br.getCityName() for br in bestRoute]
        for ii in xrange(len(myCityFrequency)):
            if myCityFrequency[ii][0] in transferCities :
                myCityFrequency[ii][1] += 1
    pairIter += 1

#print myCityFrequency
sortedFrequency = sorted(myCityFrequency, key=itemgetter(1), reverse=True)
print("10 Most common transfer cities")
for sf in sortedFrequency[:10] :
    print(sf)
print("10 Least common transfer cities")
for sf in sortedFrequency[-10:] :
    print(sf)
print("Done!")