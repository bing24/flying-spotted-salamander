print "############################################"
import time
# import classes
# simulator = classes.Simulation()
# simulator.addVehicle(5)
# simulator.addCharger(3)
# for i in range(0, 3):
#     simulator.sim(50)


import classes
env = classes.Environment()
env.visualize()
env.calculateCost()
agent = classes.Vehicle(1)
start_time = time.time()
env.explored(agent)
print "Time elapsed is:", time.time() - start_time
env.combine()
env.calculateCost()
env.visualize()
