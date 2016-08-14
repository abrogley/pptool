execfile("src/airport_list.py")
execfile("src/airports.py")

# Simple tests
airportDatabase = getAirportList()
airports = AirportManager(airportDatabase)
'''
myCity = airports.findByName('Houston')
print "My city's name is " + myCity.getCityName() + \
      " and it is located at " + str(myCity.getLocX()) + \
      " in X and " + str(myCity.getLocY()) + " in Y "

print "The distance between my city and point [3000,5000] is " + \
      str(airports.getDistanceBetween(myCity, [3000,5000]))

print "To get anywhere from my city, there is a base fare of " + \
      str(airports.baseFare) + " coins plus an extra " + \
      str(airports.coinsPerUnitDistance) + " coins per unit distance."

print "The distance between Detroit and Tokyo is " + \
      str(airports.getDistanceBetween('Detroit','Tokyo'))

print "The cost between Boston and Orlando is " + \
      str(int(airports.costBetween('Boston','Orlando')))

radius = 500
withinRangeFromMyCity = airports.findAirportsWithinRange(myCity.getCityName(), radius)
print "There are some cities close to me. The ones within " + str(radius) + \
      " distance are:"
for city in withinRangeFromMyCity :
    print "    " + city.getCityName()

sortedListWithinRangeAndClass2 = airports.findAirportsTowards(myCity, 'Seattle', radius, 2)
print "I can sort these cities by distance to Seattle and filter by class 2 and above:"
for city in sortedListWithinRangeAndClass2 :
    print "    " + city.getCityName()

#Purposely test different city input styles
cityA = airportDatabase[160]
cityB = airportDatabase[44].getCityName()

distAB = airports.getDistanceBetween(cityA,cityB)
midpt = airports.getMidpointBetween(cityA,cityB)
nearestToMidpt1 = airports.findNearestAirport(midpt, 1, Airport)
nearestToMidpt2 = airports.findNearestAirport(midpt, 2, Airport)
nearestToMidpt3 = airports.findNearestAirport(midpt, 3, Airport)
distFromMidpt1 = airports.getDistanceBetween(midpt, nearestToMidpt1)
distFromMidpt2 = airports.getDistanceBetween(midpt, nearestToMidpt2)
distFromMidpt3 = airports.getDistanceBetween(midpt, nearestToMidpt3)
best1 = airports.findBestTransferAirport(cityA, cityB, 1, 0.99*distAB, Airport)
best2 = airports.findBestTransferAirport(cityA, cityB, 2, 0.99*distAB, Airport)
best3 = airports.findBestTransferAirport(cityA, cityB, 3, 0.99*distAB, Airport)
bestReal1 = airports.findBestTransferAirport(cityA, cityB, 1, 1150, Airport)
bestReal2 = airports.findBestTransferAirport(cityA, cityB, 2, 2300, Airport)
bestReal3 = airports.findBestTransferAirport(cityA, cityB, 3, 3576, Airport)

ANCtoYWG = airports.findBestTransferAirport('Anchorage', 'Winnipeg', 1, 1150, str)
print ANCtoYWG

print "The midpoint between " + cityA.getCityName() + " and " + cityB + \
      " is " + str(midpt) + ". The nearest airports of each class" + \
      " to this midpoint are :\n\t" + \
      nearestToMidpt1.getCityName() + " which is " + str(distFromMidpt1) + " away\n\t" + \
      nearestToMidpt2.getCityName() + " which is " + str(distFromMidpt2) + " away\n\t" + \
      nearestToMidpt3.getCityName() + " which is " + str(distFromMidpt3) + " away"

print "Traveling between " + cityA.getCityName() + " and " + cityB + \
      " via each of these midpoints would add, respectively, this much extra distance:\n\t" + \
      str(airports.getDistanceBetween(cityA, nearestToMidpt1) + airports.getDistanceBetween(cityB, nearestToMidpt1) - \
          airports.getDistanceBetween(cityA, cityB)) + "\n\t" + \
      str(airports.getDistanceBetween(cityA, nearestToMidpt2) + airports.getDistanceBetween(cityB, nearestToMidpt2) - \
          airports.getDistanceBetween(cityA, cityB)) + "\n\t" + \
      str(airports.getDistanceBetween(cityA, nearestToMidpt3) + airports.getDistanceBetween(cityB, nearestToMidpt3) - \
          airports.getDistanceBetween(cityA, cityB))

print "However, these aren't necessarily the best transfer cities! The best layover airports of each class are:\n\t" + \
      best1.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best1) + airports.getDistanceBetween(cityB, best1) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance\n\t" + \
      best2.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best2) + airports.getDistanceBetween(cityB, best2) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance\n\t" + \
      best3.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best3) + airports.getDistanceBetween(cityB, best3) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance"

print "Furthermore, an airplane may not have the range to cover the distances between these cities in one go."
if bestReal1 == -1 :
    print "\tThe upgraded Mohawk cannot travel between these cities with just one transfer."
elif bestReal1.getCityName() == cityA.getCityName() or bestReal1.getCityName() == cityB :
    print "\tThe upgraded Mohawk can complete the journey between " + cityA.getCityName() + " and " + cityB + " nonstop"
else :
    print "\tThe upgraded Mohawk can travel via " + \
      bestReal1.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, bestReal1) + airports.getDistanceBetween(cityB, bestReal1) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance"
if bestReal2 == -1 :
    print "\tThe upgraded Aeroeagle cannot travel between these cities with just one transfer."
elif bestReal2.getCityName() == cityA.getCityName() or bestReal2.getCityName() == cityB :
    print "\tThe upgraded Aeroeagle can complete the journey between " + cityA.getCityName() + " and " + cityB + " nonstop"
else :
    print "\tThe upgraded Aeroeagle can travel via " + \
      bestReal2.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, bestReal2) + airports.getDistanceBetween(cityB, bestReal2) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance"
if bestReal3 == -1 :
    print "\tThe upgraded Cloudliner cannot travel between these cities with just one transfer."
elif bestReal3.getCityName() == cityA.getCityName() or bestReal3.getCityName() == cityB :
    print "\tThe upgraded Cloudliner can complete the journey between " + cityA.getCityName() + " and " + cityB + " nonstop"
else :
    print "\tThe upgraded Cloudliner can travel via " + \
      bestReal3.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, bestReal3) + airports.getDistanceBetween(cityB, bestReal3) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra distance"
'''
print "Try to determine the best route between the following city pairs using an upgraded Mohawk."
pairs = [[20,188], [0,1], [2,3], [4,5], [6,7], [8,7], [34,50]]
pairs = [[162,240]]
pairs2 = [[32,18]]
for p in pairs:
    print airportDatabase[p[0]].getCityName() + " and " + airportDatabase[p[1]].getCityName()
    bestRoute = airports.findBestRouteBetween(airportDatabase[p[0]], airportDatabase[p[1]], 1, 1150)
    for sr in bestRoute :
        print "    " + sr.getCityName()
for p in pairs2:
    midpoints = airports.getMidpointBetween(airportDatabase[p[0]], airportDatabase[p[1]], 3)
    midpointAirports = []
    for mp in midpoints:
        midpointAirports.append(airports.findNearestAirport(mp, 2, Airport))
        print midpointAirports[-1].getCityName()
        
    print airportDatabase[p[0]].getCityName() + " and " + airportDatabase[p[1]].getCityName()
    bestRoute = airports.findBestRouteBetween(airportDatabase[p[0]], airportDatabase[p[1]], 2, 2300)
    for sr in bestRoute :
        print "    " + sr.getCityName()

