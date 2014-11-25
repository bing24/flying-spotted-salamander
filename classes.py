import matplotlib.pyplot as plt
import numpy
from scipy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


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
        self.x = [5, 60, 40]
        self.y = [3, 20, 20]
        self.var = 10
        self.max_probability = .8 / (sqrt(2 * pi) * self.var)

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


class Environment:

    def __init__(self):
        self.width = 400
        self.length = 400
        self.resolution = .5
        self.var = 50  # self.length / 6
        self.xx = numpy.arange(-self.length / 2,
                               self.length / 2 + self.resolution, self.resolution)
        self.yy = numpy.arange(-self.width / 2,
                               self.width / 2 + self.resolution, self.resolution)
        self.xmesh, self.ymesh = numpy.meshgrid(self.xx, self.yy, sparse=True)
        num = exp(-(self.xmesh ** 2 + self.ymesh **
                    2) / (2 * self.var ** 2))
        denum = (sqrt(2 * pi) * self.var)
        self.probability = num / denum
        self.explored_probability = numpy.ones(shape(self.probability))

    def combine(self):
        self.probability = self.probability * self.explored_probability

    def visualize(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        xmesh, ymesh = numpy.meshgrid(self.xx, self.yy, sparse=True)
        # ax.auto_scale_xyz(
        #     [-length, length], [-length, 3 * length], [0, 2 * length])
        surf = ax.plot_wireframe(self.xmesh, self.ymesh, self.probability, rstride=20, cstride=20, cmap=cm.cool,
                                 linewidth=0.1, antialiased=True)
        plt.show()

    def explored(self, vehicle):
        monitor_length = int(3 * vehicle.var / self.resolution)
        for index in range(0, size(vehicle.x)):
            x_index = int(self.length / self.resolution / 2 +
                          round(vehicle.x[index] / self.resolution))  # TODO round all
            # print "debug: ", x_index
            y_index = int(self.width / self.resolution / 2 +
                          round(vehicle.y[index] / self.resolution))

            monitor_x_range = range(int(x_index - monitor_length), int(x_index + monitor_length))
            monitor_y_range = range(int(y_index - monitor_length), int(y_index + monitor_length))
            for x in monitor_x_range:
                for y in monitor_y_range:
                    distance_square = (
                        self.resolution * (x - x_index)) ** 2 + (self.resolution * (y - y_index)) ** 2
                    # print distance_square
                    num = exp(-distance_square / (2 * vehicle.var ** 2))
                    denum = vehicle.var * sqrt(2 * pi)
                    temp_probability = num / denum
                    self.explored_probability[x][y] = min([1 - temp_probability / vehicle.max_probability, self.explored_probability[x][y]])
                    if self.explored_probability[x][y] < 0:
                        self.explored_probability[x][y] = 0
                # print self.explored_probability
        # grid = numpy.arrange(vehicle.x)
        # self.probability[vehicle.x][vehicle.y] = 0

    def calculateCost(self):
        self.cost = self.probability.sum() * self.resolution ** 2
        print "Cost is:", self.cost
