exec(open("src/AirportDatabase.py").read())
exec(open("src/AirportManager.py").read())

# Simple tests
airportDatabase = getAirportList()
airports = AirportManager(airportDatabase)
airports.debugPrint = False

#Purposely test different city input styles
cityA = 'New York'
cityB = 'Cairo'

distAB = airports.getDistanceBetween(cityA,cityB)
vecAB = airports.findVector(cityA,cityB)
print( vecAB )

midpt = airports.getMidpointBetween(cityA,cityB)
nearestToMidpt1 = airports.findNearestAirport(midpt, 1, Airport)
nearestToMidpt2 = airports.findNearestAirport(midpt, 2, Airport)
nearestToMidpt3 = airports.findNearestAirport(midpt, 3, Airport)

# FIXME. getDistanceBetween should accept doubly bracketed locations [[x, y]]
distFromMidpt1 = airports.getDistanceBetween(midpt[0], nearestToMidpt1)
distFromMidpt2 = airports.getDistanceBetween(midpt[0], nearestToMidpt2)
distFromMidpt3 = airports.getDistanceBetween(midpt[0], nearestToMidpt3)

best1 = airports.findBestTransferAirport(cityA, cityB, 1, 0.99*distAB, Airport)
best2 = airports.findBestTransferAirport(cityA, cityB, 2, 0.99*distAB, Airport)
best3 = airports.findBestTransferAirport(cityA, cityB, 3, 0.99*distAB, Airport)
bestReal1 = airports.findBestTransferAirport(cityA, cityB, 1, 1150, Airport)
bestReal2 = airports.findBestTransferAirport(cityA, cityB, 2, 2300, Airport)
bestReal3 = airports.findBestTransferAirport(cityA, cityB, 3, 3576, Airport)

ANCtoYWG = airports.findBestTransferAirport('Anchorage', 'Winnipeg', 1, 1150, str)
print( ANCtoYWG )

print( "The midpoint between " + cityA + " and " + cityB + \
      " is " + str(midpt) + ". The nearest airports of each class" + \
      " to this midpoint are :\n\t" + \
      nearestToMidpt1.getCityName() + " which is " + str(distFromMidpt1) + " away and adds " + \
      str(airports.getDistanceBetween(cityA, nearestToMidpt1) + airports.getDistanceBetween(cityB, nearestToMidpt1) - \
      airports.getDistanceBetween(cityA, cityB)) + " extra distance\n\t" + \
      nearestToMidpt2.getCityName() + " which is " + str(distFromMidpt2) + " away and adds " + \
      str(airports.getDistanceBetween(cityA, nearestToMidpt2) + airports.getDistanceBetween(cityB, nearestToMidpt2) - \
      airports.getDistanceBetween(cityA, cityB)) + " extra distance\n\t" + \
      nearestToMidpt3.getCityName() + " which is " + str(distFromMidpt3) + " away and adds " + \
      str(airports.getDistanceBetween(cityA, nearestToMidpt3) + airports.getDistanceBetween(cityB, nearestToMidpt3) - \
      airports.getDistanceBetween(cityA, cityB)) + " extra distance" )

print( "However, these aren't necessarily the best transfer cities! The best layover airports of each class are:\n\t" + \
      best1.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best1) + airports.getDistanceBetween(cityB, best1) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance\n\t" + \
      best2.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best2) + airports.getDistanceBetween(cityB, best2) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance\n\t" + \
      best3.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best3) + airports.getDistanceBetween(cityB, best3) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance" )
          
print( "Furthermore, an airplane may not have the range to cover the distances between these cities in one go." )
if bestReal1 < 0 :
    print( "\tThe upgraded Mohawk cannot travel between these cities with just one transfer." )
elif bestReal1.getCityName() == cityA or bestReal1.getCityName() == cityB :
    print( "\tThe upgraded Mohawk can complete the journey between " + cityA + " and " + cityB + " nonstop" )
else :
    print( "\tThe upgraded Mohawk can travel via " + \
      bestReal1.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, bestReal1) + airports.getDistanceBetween(cityB, bestReal1) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance" )
if bestReal2 < 0 :
    print( "\tThe upgraded Aeroeagle cannot travel between these cities with just one transfer." )
elif bestReal2.getCityName() == cityA or bestReal2.getCityName() == cityB :
    print( "\tThe upgraded Aeroeagle can complete the journey between " + cityA + " and " + cityB + " nonstop" )
else :
    print( "\tThe upgraded Aeroeagle can travel via " + \
      bestReal2.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, bestReal2) + airports.getDistanceBetween(cityB, bestReal2) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance" )
if bestReal3 < 0 :
    print( "\tThe upgraded Cloudliner cannot travel between these cities with just one transfer." )
elif bestReal3.getCityName() == cityA or bestReal3.getCityName() == cityB :
    print( "\tThe upgraded Cloudliner can complete the journey between " + cityA + " and " + cityB + " nonstop" )
else :
    print( "\tThe upgraded Cloudliner can travel via " + \
      bestReal3.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, bestReal3) + airports.getDistanceBetween(cityB, bestReal3) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance" )

print( "Try to determine the best route between the following city pairs using an upgraded Mohawk." )

pairs = [ \
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
    bestRoute = airports.findBestRouteBetween(airportDatabase[p[0]], airportDatabase[p[1]], 1, 1150)
    for sr in bestRoute :
        if ii > 0:
            cumRange += airports.getDistanceBetween(bestRoute[ii-1], bestRoute[ii])
        print( "    " + sr.getCityName() )
        ii += 1
    perfectRange = airports.getDistanceBetween(bestRoute[0], bestRoute[-1])
    rangePct = (cumRange/perfectRange-1)*100
    print( "        Range on this route: " + str(cumRange) )
    print( "        Straight Line Range: " + str(perfectRange) )
    print( "        Percentage increase: " + '{:2.2f}'.format(rangePct) + "%" )

print( "Try to determine the best route between the following city pairs using an upgraded Aeroeagle." )
pairs2 = [[32,18], [90,219], [84,204], [156,67]]

for p in pairs2:
    cumRange = 0
    ii = 0
    print( airportDatabase[p[0]].getCityName() + " and " + airportDatabase[p[1]].getCityName() )
    bestRoute = airports.findBestRouteBetween(airportDatabase[p[0]], airportDatabase[p[1]], 2, 2300)
    for sr in bestRoute :
        if ii > 0:
            cumRange += airports.getDistanceBetween(bestRoute[ii-1], bestRoute[ii])
        print( "    " + sr.getCityName() )
        ii += 1
    perfectRange = airports.getDistanceBetween(bestRoute[0], bestRoute[-1])
    rangePct = (cumRange/perfectRange-1)*100
    print( "        Range on this route: " + str(cumRange) )
    print( "        Straight Line Range: " + str(perfectRange) )
    print( "        Percentage increase: " + '{:2.2f}'.format(rangePct) + "%" )

print("Done!")