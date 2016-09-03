exec(open("src/AirportDatabase.py").read())
exec(open("src/AirportManager.py").read())
exec(open("src/RouteManager.py").read())

# Simple tests
airportDatabase = getAirportList()
airports = AirportManager(airportDatabase)
router = RouteManager(airports)
airports.debugPrint = False


'''
print( "Try to determine the best route between the following city pairs using an upgraded Mohawk." )

pairs = [
    [20,188],
    [0,1],
    [2,3],
    [4,5],
    [6,7],
    [8,7],
    [34,50],
    [162,240],
    [90,71]
    ]

for p in pairs:
    cumRange = 0
    ii = 0
    print( airportDatabase[p[0]].getCityName() + " and " + airportDatabase[p[1]].getCityName() )
    bestRoute = router.findBestRouteBetween(airportDatabase[p[0]], airportDatabase[p[1]], 1, 1150)
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

print( "Try to determine the best route between the following city pairs using an upgraded Aeroeagle." )
pairs2 = [[32,18], [90,219], [84,204], [156,67]]

for p in pairs2:
    cumRange = 0
    ii = 0
    print( airportDatabase[p[0]].getCityName() + " and " + airportDatabase[p[1]].getCityName() )
    bestRoute = router.findBestRouteBetween(airportDatabase[p[0]], airportDatabase[p[1]], 2, 2300)
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

print("Done!")
'''