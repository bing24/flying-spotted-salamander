import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
print "######################## 2D simulation ################"

base_distance=10000.0 # m
explorer_speed=9000.0 # m/hr
explorer_operation_time=5.0 # hr
explorer_operation_distance=explorer_speed*explorer_operation_time
recharge_time=3.5 # hr
number_of_rechargers=4
charger_speed=4000.0 # m/hr


travel_time=[]
deploy_time=[]

for i in range(0,number_of_rechargers):
	distance=base_distance+(i+1)*explorer_operation_distance
	time=distance/charger_speed
	travel_time.append(time)
	deploy_time.append((i+1)*explorer_operation_time+i*recharge_time-travel_time[i])
	print "Recharger #",i+1,"should be deployed",deploy_time[i],"hours relative to start of mission"
total_length=(number_of_rechargers+1)*explorer_operation_distance
total_time=total_length/explorer_speed+number_of_rechargers*recharge_time
print "Total exploration length was",total_length
print "Total operation time was",total_time
print "Total downtime was",number_of_rechargers*recharge_time

time_step=.05
time_start=min(deploy_time)
# for i in range(0,len(travel_time)):
# 	travel_time[i]=time_start-travel_time[i]
print time_start,travel_time,deploy_time


fig = plt.figure()
ax = plt.axes(xlim=(1.2*-base_distance, 1.2*total_length), ylim=(-2, 2))
iver, = ax.plot([], [],'ko', lw=2)
chargers_x=[-base_distance,-base_distance,-base_distance,-base_distance]
chargers_y=[0,0,0,0]
chargers, = ax.plot([], [],'ro', lw=2)
stop=[False,False,False,False]
# initialization function: plot the background of each frame
def init():
    iver.set_data([], [])
    chargers.set_data([],[])
    return iver,chargers

# animation function.  This is called sequentially
def animate(i):
    time=i*time_step+time_start
    for i in range(0,number_of_rechargers):
    	# if time-(travel_time[i]+deploy_time[i])<recharge_time:
    	# 	stop[i]=True
    	# else:
    	stop[i]=(time-(travel_time[i]+deploy_time[i])<recharge_time)
    	if time>(deploy_time[i]) and time<(travel_time[i]+deploy_time[i]):
	    	chargers_x[i]=(time-deploy_time[i])*charger_speed-base_distance
    if time>=0:
    	if not any(stop):
	    	iver_x = (time)*explorer_speed
	    	iver_y =0
	else:
		iver_x=0
		iver_y=0
    iver.set_data(iver_x, iver_y)
    chargers.set_data(chargers_x,chargers_y)
    return iver,chargers

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=700, interval=5, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
