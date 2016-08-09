execfile("src/airports.py")

# Simple tests
myList = AirportList()

myCity = myList.findByName('Houston')
print "My city's name is " + myCity.getCityName() + \
      " and it is located at " + str(myCity.getLocX()) + \
      " in X and " + str(myCity.getLocY()) + " in Y "

print "To get anywhere from my city, there is a base fare of " + \
      str(myList.baseFare) + " coins plus an extra " + \
      str(myList.coinsPerUnitDistance) + " coins per unit distance."

print "The distance between Detroit and Tokyo is " + \
      str(myList.distanceBetween('Detroit','Tokyo'))

print "The cost between Boston and Orlando is " + \
      str(int(myList.costBetween('Boston','Orlando')))

radius = 500
withinRangeFromMyCity = myList.findAirportsWithinRange(myCity.getCityName(), radius)
withinRangeFromMyCityAndClass2 = myList.findAirportsWithinRange(myCity.getCityName(), radius, 2)
print "There are some cities close to me. The ones within " + str(radius) + \
      " distance are:"
for city in withinRangeFromMyCity :
    print "    " + city.getCityName()
print "The ones that are class 2 or greater are:"
for city in withinRangeFromMyCityAndClass2 :
    print "    " + city.getCityName()
