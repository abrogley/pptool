class Airport(object):
    "airport class"
    def __init__(self, airportName="", airportClass=0, loc=[0,0]):
        self.airportName = airportName
        self.airportClass = airportClass
        self.loc = loc

    def getCityName(self):
        return self.airportName

    def getClass(self):
        return self.airportClass

    def getLoc(self):
        return self.loc

    def getLocX(self):
        return self.loc[0]

    def getLocY(self):
        return self.loc[1]
