class client(object):

    """docstring for client"""

    def __init__(self, id):
        super(client, self).__init__()
        self.total_operation_time = 10 * 60
        self.operation_time = 0
        self.total_charging_time = 10 * 60
        self.charge_ratio = 1
        self.id = id
        self.on_charge = False
        self.operating = False

    def operate(self, timestep):
        self.operation_time += timestep
        self.charge_ratio -= (self.total_charging_time /
                              self.total_operation_time) * timestep

    def getOperationTimeLeft(self):
        return self.total_operation_time - self.operation_time

    def getLifeRatioleft(self):
        return self.getOperationTimeLeft() / self.total_operation_time

    def charge(self, timestep):
        self.charge_ratio += timestep / self.total_charging_time

    def getChargingRatio(self):
        return self.charge_ratio
