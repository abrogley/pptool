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

class AirportList(object):
    "class with many operations available for the list of airports"
    def __init__(self, inputList=""):
        "Airport coordinates from some input source"
        if inputList :
            self.airports = inputList
        else :
            "This is the default list"
            self.baseFare             = 50
            self.coinsPerUnitDistance = 0.25
            self.airports = [
                Airport('Adelaide', 1, [9852,6288]),
                Airport('Aden', 1, [7056,4752]),
                Airport('Ahmedabad', 2, [7864,4472]),
                Airport('Al Fashir', 1, [6404,4696]),
                Airport('Algiers', 2, [5768,3992]),
                Airport('Alice Springs', 1, [9724,5928]),
                Airport('Amsterdam', 1, [5844,3320]),
                Airport('Anadyr', 1, [10996,2592]),
                Airport('Anchorage', 1, [1180,2828]),
                Airport('Araguaina', 1, [4228,5352]),
                Airport('Asuncion', 1, [3972,5988]),
                Airport('Athens', 1, [6396,3928]),
                Airport('Atlanta', 2, [3164,4112]),
                Airport('Auckland', 1, [10908,6352]),
                Airport('Baghdad', 2, [6984,4080]),
                Airport('Bamako', 1, [5476,4768]),
                Airport('Bangalore', 3, [8004,4780]),
                Airport('Bangkok', 3, [8680,4752]),
                Airport('Barcelona', 2, [5740,3808]),
                Airport('Bariloche', 1, [3548,6568]),
                Airport('Barrow', 1, [1008,2084]),
                Airport('Beijing', 3, [9180,3864]),
                Airport('Beira', 1, [6696,5776]),
                Airport('Beirut', 1, [6772,4080]),
                Airport('Belem', 1, [4216,5196]),
                Airport('Belfast', 1, [5472,3220]),
                Airport('Belgrade', 1, [6312,3648]),
                Airport('Benghazi', 1, [6288,4168]),
                Airport('Bergen', 1, [5832,2892]),
                Airport('Berlin', 2, [6112,3324]),
                Airport('Bern', 1, [5920,3544]),
                Airport('Bismarck', 1, [2572,3592]),
                Airport('Bogota', 2, [3440,4980]),
                Airport('Bordeaux', 1, [5668,3640]),
                Airport('Boston', 2, [3540,3760]),
                Airport('Brasilia', 1, [4176,5676]),
                Airport('Brisbane', 1, [10260,6056]),
                Airport('Broken Hill', 1, [9944,6200]),
                Airport('Broome', 1, [9376,5672]),
                Airport('Brussels', 1, [5816,3412]),
                Airport('Bucharest', 1, [6604,3648]),
                Airport('Buenos Aires', 3, [3952,6300]),
                Airport('Butwal', 1, [8176,4312]),
                Airport('Cairns', 1, [10028,5696]),
                Airport('Cairo', 3, [6584,4252]),
                Airport('Calgary', 1, [2308,3328]),
                Airport('Campo Grande', 1, [4008,5808]),
                Airport('Cancun', 1, [3068,4532]),
                Airport('Capetown', 1, [6228,6220]),
                Airport('Caracas', 2, [3640,4836]),
                Airport('Casablanca', 1, [5456,4124]),
                Airport('Cebu', 1, [9416,4856]),
                Airport('Charleston', 1, [3292,4140]),
                Airport('Chengdu', 2, [8656,4204]),
                Airport('Chicago', 3, [3028,3724]),
                Airport('Chihuahua', 1, [2524,4280]),
                Airport('Christchurch', 1, [10848,6600]),
                Airport('Cincinnati', 1, [3164,3900]),
                Airport('Copenhagen', 1, [6064,3132]),
                Airport('Cordoba', 1, [3796,6164,]),
                Airport('Cuiaba', 1, [3952,5636]),
                Airport('Cuzco', 1, [3536,5560]),
                Airport('Dakar', 1, [5184,4716]),
                Airport('Dallas', 2, [2768,4144]),
                Airport('Darwin', 1, [9628,5540]),
                Airport('Delhi', 3, [7972,4272]),
                Airport('Denver', 1, [2500,3860]),
                Airport('Detroit', 2, [3188,3780]),
                Airport('Dhaka', 3, [8376,4436]),
                Airport('Djibouti', 1, [7008,4800]),
                Airport('Durban', 1, [6596,6104]),
                Airport('Easter Island', 1, [2396,5980]),
                Airport('Edmonton', 1, [2336,3192]),
                Airport('Fairbanks', 1, [1240,2612]),
                Airport('Fortaleza', 1, [4484,5264]),
                Airport('Georgetown', 1, [3940,4968]),
                Airport('Geraldton', 1, [9132,6028]),
                Airport('Glasgow', 1, [5568,3124]),
                Airport('Goose Bay', 1, [3808,3156]),
                Airport('Guangzhou', 2, [9060,4420]),
                Airport('Guatemala', 2, [2960,4712]),
                Airport('Hammerfest', 1, [6408,2152]),
                Airport('Hanoi', 2, [8840,4528]),
                Airport('Harare', 1, [6776,5516]),
                Airport('Harbin', 2, [9476,3600]),
                Airport('Havana', 1, [3180,4480]),
                Airport('Helsinki', 1, [6424,2872]),
                Airport('Hilo', 1, [1072,4576]),
                Airport('Hobart', 1, [10092,6576]),
                Airport('Hong Kong', 2, [9116,4468]),
                Airport('Honolulu', 2, [916,4476]),
                Airport('Houston', 2, [2812,4272]),
                Airport('Hyderabad', 2, [8040,4652]),
                Airport('In Salah', 1, [5696,4344]),
                Airport('Inuvik', 1, [1668,2316]),
                Airport('Iqualit', 1, [3636,2656]),
                Airport('Iquitos', 1, [3520,5280]),
                Airport('Istanbul', 3, [6568,3832]),
                Airport('Jakarta', 3, [8892,5356]),
                Airport('Jerusalem', 1, [6740,4168]),
                Airport('Johannesburg', 2, [6484,5968]),
                Airport('Juba', 1, [6648,4992]),
                Airport('Juneau', 1, [1676,3084]),
                Airport('Kabul', 1, [7776,4048]),
                Airport('Kaduna', 1, [5904,4828]),
                Airport('Kalgoorlie', 1, [9384,6124]),
                Airport('Kampala', 1, [6668,5124]),
                Airport('Kananga', 1, [6388,5372]),
                Airport('Kandahar', 1, [7644,4148]),
                Airport('Kansas City', 1, [2796,3896]),
                Airport('Karachi', 3, [7684,4384]),
                Airport('Katherine', 1, [9676,5632]),
                Airport('Ketchikan', 1, [1804,3212]),
                Airport('Khartoum', 2, [6668,4716]),
                Airport('Kiev', 1, [6680,3420]),
                Airport('Kinshasa', 3, [6104,5248]),
                Airport('Kisangani', 1, [6428,5084]),
                Airport('Kolkata', 3, [8296,4488]),
                Airport('Kuching', 1, [8984,5140]),
                Airport('Kuwait City', 1, [7100,4248]),
                Airport('La Paz', 1, [3644,5712]),
                Airport('Lagos', 3, [5808,4964]),
                Airport('Las Vegas', 1, [2264,4008]),
                Airport('Lhasa', 1, [8400,4216]),
                Airport('Lilongwe', 1, [6720,5596]),
                Airport('Lima', 3, [3348,5428]),
                Airport('Lisbon', 1, [5420,3884]),
                Airport('Livingstone', 1, [6444,5676]),
                Airport('Lobito', 1, [6116,5528]),
                Airport('London', 3, [5640,3380]),
                Airport('Los Angeles', 3, [2104,4092]),
                Airport('Lulea', 1, [6332,2560]),
                Airport('Lyon', 1, [5820,3620]),
                Airport('Madrid', 2, [5580,3820]),
                Airport('Magadan', 1, [10244,2936]),
                Airport('Mahajanga', 1, [7076,5664]),
                Airport('Manaus', 1, [3888,5224]),
                Airport('Manchester', 1, [5588,3268]),
                Airport('Manila', 3, [9304,4728]),
                Airport('Melbourne', 2, [10024,6364]),
                Airport('Mexico City', 3, [2732,4580]),
                Airport('Miami', 2, [3276,4384]),
                Airport('Minneapolis', 1, [2876,3632]),
                Airport('Minsk', 1, [6576,3228]),
                Airport('Mogadishu', 1, [7072,5092]),
                Airport('Mombasa', 1, [6852,5280]),
                Airport('Monrovia', 1, [5356,4972]),
                Airport('Monterrey', 2, [2684,4344]),
                Airport('Montreal', 1, [3464,3648]),
                Airport('Moscow', 3, [6876,3120]),
                Airport('Mount Isa', 1, [9872,5820]),
                Airport('Mumbai', 3, [7880,4588]),
                Airport('Munich', 1, [6028,3512]),
                Airport('Murmansk', 1, [6660,2248]),
                Airport('Muscat', 1, [7432,4444]),
                Airport('Nagasaki', 1, [9580,4128]),
                Airport('Nairobi', 2, [6772,5200]),
                Airport('Nanping', 1, [9184,4328]),
                Airport('Naples', 1, [6128,3840]),
                Airport('New Orleans', 1, [2976,4236]),
                Airport('New York', 3, [3456,3824]),
                Airport('Newman', 1, [9340,5920]),
                Airport('Nome', 1, [708,2628]),
                Airport('Norilsk', 1, [8292,2304]),
                Airport('Novosibirsk', 1, [8252,3192]),
                Airport('Nuuk', 1, [4192,2716]),
                Airport('Oaxaca', 1, [2796,4644]),
                Airport('Orlando', 1, [3224,4288]),
                Airport('Osaka', 2, [9732,4068]),
                Airport('Oslo', 1, [5980,2944]),
                Airport('Ottawa', 1, [3352,3648]),
                Airport('Oulu', 1, [6476,2592]),
                Airport('Padang', 1, [8716,5212]),
                Airport('Palu', 1, [9280,5196]),
                Airport('Panama', 1, [3312,4884]),
                Airport('Paris', 3, [5744,3484]),
                Airport('Perm', 1, [7404,3020]),
                Airport('Perth', 1, [9168,6176]),
                Airport('Pevek', 1, [10836,2232]),
                Airport('Philadelphia', 2, [3392,3888]),
                Airport('Phoenix', 2, [2420,4124]),
                Airport('Port Elizabeth', 1, [6464,6220]),
                Airport('Port Hedland', 1, [9304,5796]),
                Airport('Port Moresby', 1, [10132,5472]),
                Airport('Port Sudan', 1, [6772,4596]),
                Airport('Portland', 1, [1964,3660]),
                Airport('Porto Velho', 1, [3764,5396]),
                Airport('Prague', 1, [6148,3436]),
                Airport('Punta Arenas', 1, [3592,7108]),
                Airport('Quebec', 1, [3520,3560]),
                Airport('Quito', 1, [3308,5180]),
                Airport('Rangoon', 2, [8548,4668]),
                Airport('Recife', 2, [4616,5408]),
                Airport('Reykjavik', 1, [5000,2624]),
                Airport('Riga', 1, [6416,3088]),
                Airport('Rio de Janeiro', 3, [4376,5864]),
                Airport('Riyadh', 2, [7040,4408]),
                Airport('Rockhampton', 1, [10212,5924]),
                Airport('Rome', 1, [6032,3768]),
                Airport('Salt Lake City', 1, [2292,3820]),
                Airport('Salvador', 2, [4504,5540]),
                Airport('San Diego', 1, [2176,4164]),
                Airport('San Francisco', 2, [2016,3924]),
                Airport('San Jose', 1, [3156,4848]),
                Airport('Santiago', 2, [3528,6200]),
                Airport('Santo Domingo', 1, [3552,4600]),
                Airport('Sao Paolo', 3, [4248,5920]),
                Airport('Sapporo', 1, [9916,3744]),
                Airport('Saskatoon', 1, [2540,3280]),
                Airport('Seattle', 2, [1964,3544]),
                Airport('Sendai', 1, [9908,3924]),
                Airport('Seoul', 3, [9488,3956]),
                Airport('Shanghai', 3, [9292,4208]),
                Airport('Shenyang', 3, [9380,3792]),
                Airport('Singapore', 2, [8756,5088]),
                Airport('Spokane', 1, [2200,3568]),
                Airport('St. Louis', 1, [2948,3924]),
                Airport('St. Petersburg', 2, [6580,2900]),
                Airport('Stockholm', 1, [6204,2944]),
                Airport('Sydney', 2, [10188,6260]),
                Airport('Taipei', 2, [9316,4408]),
                Airport('Tbilisi', 1, [6984,3744]),
                Airport('Tehran', 3, [7188,3988]),
                Airport('Teresina', 1, [4360,5312]),
                Airport('Thunder Bay', 1, [2996,3488]),
                Airport('Tiksi', 1, [9536,2056]),
                Airport('Timbuktu', 1, [5596,4648]),
                Airport('Tokyo', 3, [9868,4056]),
                Airport('Toronto', 2, [3268,3700]),
                Airport('Tripoli', 1, [6024,4152]),
                Airport('Trondheim', 1, [5960,2700]),
                Airport('Ulan Bator', 1, [8884,3544]),
                Airport('Urumqi', 1, [8348,3696]),
                Airport('Vancouver', 1, [1952,3424]),
                Airport('Venice', 1, [6032,3636]),
                Airport('Vienna', 1, [6212,3512]),
                Airport('Vladivostok', 1, [9608,3732]),
                Airport('Volgograd', 1, [6984,3488]),
                Airport('Warsaw', 1, [6312,3324]),
                Airport('Washington D.C.', 2, [3356,3952]),
                Airport('Wellington', 1, [10940,6508]),
                Airport('Whitehorse', 1, [1612,2892]),
                Airport('Windhoek', 1, [6208,5872]),
                Airport('Winnipeg', 1, [2756,3448]),
                Airport('Xi\'an', 3, [9000,4084]),
                Airport('Xining', 1, [8632,3980]),
                Airport('Yakutsk', 1, [9576,2804]),
                Airport('Yellowknife', 1, [2264,2764]),
                Airport('Yinchuan', 1, [8876,3896]),
                Airport('Zanzibar', 1, [6856,5392]) ]

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

    "Find distance between two cities by their names"
    def distanceBetween(self, firstAirportName, secondAirportName):
        firstAirport = self.findByName(firstAirportName)
        secondAirport = self.findByName(secondAirportName)
        xDistance = secondAirport.getLocX() - firstAirport.getLocX()
        yDistance = secondAirport.getLocY() - firstAirport.getLocY()
        distance = (xDistance**2 + yDistance**2)**0.5
        return distance

    "Find the job cost (payout) between two cities by their names"
    def costBetween(self, firstAirportName, secondAirportName):
        cost = self.distanceBetween(firstAirportName, secondAirportName) * self.coinsPerUnitDistance + self.baseFare
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
            
            if (self.distanceBetween(airportName, candidateAirport.getCityName()) < rangeDistance) :
                subsetWithinRange.append(candidateAirport)
                
        return subsetWithinRange
