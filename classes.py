class Vehicle:

    """docstring for Vehicle"""

    def __init__(self, id):
        self.total_battery_life = 10 * 60
        self.battery_life = self.total_battery_life
        self.total_charging_time = 10 * 60
        self.charge_ratio = 1
        self.id = id
        self.on_charge = False
        self.operating = True

    def operate(self, timestep):
        self.on_charge = False
        if self.battery_life <= 0.05:
            print "vehicle with ID: " + self.id + " is about to decline."
        if self.battery_life <= 0:
            print "vehicle with ID: " + self.id + " declined."
        self.battery_life -= timestep
        self.charge_ratio -= (self.total_charging_time /
                              self.total_battery_life) * timestep

    def getBatteryTimeLeft(self):
        return self.battery_life

    def getLifeRatioleft(self):
        return self.getBatteryTimeLeft() / self.total_battery_life

    def charge(self, timestep):
        self.operate = False
        self.charge_ratio += timestep / self.total_charging_time
        self.battery_life += timestep * \
            (self.total_battery_life / self.total_charging_time)

    def getChargeRatio(self):
        return self.charge_ratio

    def goForCharge(self):
        print self.getChargeRatio()
        if self.getChargeRatio() < .5:
            self.on_charge = True
            self.operate = False
            print "Vehicle " + str(self.id) + " went for charging"


class Charger:

    """docstring for Charger"""

    def __init__(self, id):
        self.id = id
        self.queue = []

    def queue(self, vehicle):
        self.queue.append(vehicle)

    def power(self, timestep):
        if self.queue:
            self.queue(0).charge(timestep)

    def moveQueue(self):
        if self.queue:
            del self.queue[0]

    def deploy(self):
        if self.queue:
            if self.queue[0].getChargeRatio() > .9:
                self.queue[0].on_charge = False
                self.queue[0].operating = True
                print "Charger " + self.id + " deployed vehicle " + str(self.queue[0].id)


class Simulation:

    """docstring for Simulation"""

    def __init__(self):
        self.vehicles = []
        self.chargers = []

    def addVehicle(self, this_many=1):
        for time in range(0, this_many):
            new_id = len(self.vehicles)
            self.vehicles.append(Vehicle(new_id))
            print "Vehicle " + str(new_id) + " was added"

    def addCharger(self, this_many=1):
        for time in range(0, this_many):
            new_id = len(self.chargers)
            self.chargers.append(Charger(new_id))
            print "Charger " + str(new_id) + " was added"

    def sim(self, timestep):
        print "Running simulation for extra " + str(timestep) + " minutes"
        for vehicle in self.vehicles:
            vehicle.goForCharge()
            if vehicle.operating:
                vehicle.operate(timestep)
                print "Vehicle" + str(vehicle.id) + " operated for" + str(timestep) + "minutes"
            if vehicle.on_charge:
                vehicle.charge(timestep)

        for charger in self.chargers:
            charger.deploy()
            charger.power(timestep)
            print "Charger " + str(charger.id) + " charged for " + str(timestep) + " minutes"
