print "############################################"
import classes
simulator = classes.Simulation()
simulator.addVehicle(5)
simulator.addCharger(3)
for i in range(0, 3):
    simulator.sim(50)
