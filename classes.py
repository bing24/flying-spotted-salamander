class Vehicle:

    """docstring for Vehicle"""

    def __init__(self, id):
        super(Vehicle, self).__init__()
        self.total_battery_life = 10 * 60
        self.battery_life = self.total_battery_life
        self.total_charging_time = 10 * 60
        self.charge_ratio = 1
        self.id = id
        self.on_charge = False
        self.operating = False

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

    def getChargingRatio(self):
        return self.charge_ratio

    def goForCharge(self):
        if self.charge_ratio() < .05:
            self.on_charge = True
            self.operate = False


class Charger:

    """docstring for Charger"""

    def __init__(self, id):
        super(Charger, self).__init__()
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
        if self.queue(0).charge_ratio() > .9:
            self.queue(0).on_charge = False
            self.queue(0).operating = True


class Simulation:

    """docstring for Simulation"""

    def __init__(self):
        self.vehicles = []
        self.chargers = []

    def addVehicle(self, this_many=1):
        for time in range(0, this_many):
            new_id = len(Simulation).vehicles
            self.vehicles.append(Vehicle(new_id))

    def addCharger(self, this_many=1):
        for time in range(0, this_many):
            new_id = len(Simulation).chargers
            self.chargers.append(Charger(new_id))

    def sim(self, timestep):
        for vehicle in self.vehicles:
            vehicle.goForCharge()
            if vehicle.operating:
                vehicle.operate(timestep)
            if vehicle.on_charge:
                vehicle.charge(timestep)

        for charger in self.chargers:
            charger.deploy()
            charger.power()
