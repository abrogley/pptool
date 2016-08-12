execfile("src/airport_list.py")
execfile("src/airports.py")

# Simple tests
airportDatabase = getAirportList()
airports = AirportManager(airportDatabase)

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

#Purposely test different city input styles
cityA = airportDatabase[160]
cityB = airportDatabase[41].getCityName()
cityB = "Bangalore"

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
          airports.getDistanceBetween(cityA, cityB)) + " extra\n\t" + \
      best2.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best2) + airports.getDistanceBetween(cityB, best2) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra\n\t" + \
      best3.getCityName() + " which is " + str(airports.getDistanceBetween(cityA, best3) + airports.getDistanceBetween(cityB, best3) - \
          airports.getDistanceBetween(cityA, cityB)) + " extra"

print "The cost between Boston and Orlando is " + \
      str(int(airports.costBetween('Boston','Orlando')))

radius = 500
withinRangeFromMyCity = airports.findAirportsWithinRange(myCity.getCityName(), radius)
withinRangeFromMyCityAndClass2 = airports.findAirportsWithinRange(myCity.getCityName(), radius, 2)
print "There are some cities close to me. The ones within " + str(radius) + \
      " distance are:"
for city in withinRangeFromMyCity :
    print "    " + city.getCityName()
print "The ones that are class 2 or greater are:"
for city in withinRangeFromMyCityAndClass2 :
    print "    " + city.getCityName()

