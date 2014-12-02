import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
print "######################## 2D simulation ################"
print "boner"

# initialization function: plot the background of each frame

class anim(object):
    def __init__(self):
        self.base_distance=90000.0 # m
        self.explorer_speed=9000.0 # m/hr
        explorer_operation_time=5.0 # hr
        explorer_operation_distance=self.explorer_speed*explorer_operation_time
        self.recharge_time=3.5 # hr
        self.number_of_rechargers=1
        self.charger_speed=4000.0 # m/hr
        self.iver_x=0
        self.iver_y=.1
        self.stop_time=[]

        self.travel_time=[]
        self.deploy_time=[]

        for i in range(0,self.number_of_rechargers):
            distance=self.base_distance+(i+1)*explorer_operation_distance
            time=distance/self.charger_speed
            self.travel_time.append(time)
            self.deploy_time.append((i+1)*explorer_operation_time+i*self.recharge_time-self.travel_time[i])
            print "Recharger #",i+1,"should be deployed",self.deploy_time[i],"hours relative to start of mission. It gets to its destination after",self.travel_time[i],"hours and its total travel distance is",distance,"meters"
        self.total_length=(self.number_of_rechargers+1)*explorer_operation_distance
        total_time=self.total_length/self.explorer_speed+self.number_of_rechargers*self.recharge_time
        print "Total exploration length was",self.total_length
        print "Total operation time was",total_time
        print "Total downtime was",self.number_of_rechargers*self.recharge_time
        for i in range(0,self.number_of_rechargers):
            self.stop_time.append(0)
            self.stop_time[i]=self.travel_time[i]+self.deploy_time[i]
        self.time_start=min(self.deploy_time)

        self.chargers_x=[-self.base_distance,-self.base_distance,-self.base_distance,-self.base_distance]
        self.chargers_y=[0,0,0,0]
        
        
    def setup(self):
        iver.set_data([], [])
        chargers.set_data([],[])
        time_text.set_text('')
        state_text.set_text('')
        return iver,chargers,time_text,state_text

    # animation function.  This is called sequentially
    def animate(self,i):
        stop=[False,False,False,False]
        time_step=.05
        time=i*time_step+self.time_start
        time_text.set_text('time = %.1f hr' % time)
        for i in range(0,self.number_of_rechargers):

            stop[i]=(time-self.stop_time[i]<=self.recharge_time)and(time>self.stop_time[i])
            if time>=(self.deploy_time[i]) and time<=(self.stop_time[i]):
                self.chargers_x[i]=time_step*self.charger_speed+self.chargers_x[i]
            if time>self.stop_time[i]+self.recharge_time:
                self.chargers_x[i]=-time_step*self.charger_speed+self.chargers_x[i]
                if self.chargers_x[i]<-self.base_distance:
                    self.chargers_x[i]=-self.base_distance
        if time>0:
            if not any(stop):
                state_text.set_text('Status of the mission: Exploring')
                self.iver_x = time_step*self.explorer_speed+self.iver_x
            else:
                state_text.set_text('Status of the mission: Recharging')
        else:
            state_text.set_text('Status of the mission: Not started yet')
        if self.iver_x>self.total_length:
            self.iver_x=self.total_length
            state_text.set_text('Status of the mission: End of mission')
        iver.set_data(self.iver_x, self.iver_y)
        chargers.set_data(self.chargers_x,self.chargers_y)
        return iver,chargers,time_text,state_text

anime=anim()
fig = plt.figure()
ax = plt.axes(xlim=(1.2*-anime.base_distance, 1.2*anime.total_length), ylim=(-2, 2))

iver, = ax.plot([], [],'ko', lw=2,markersize=10)
chargers, = ax.plot([], [],'ro', lw=2,marker='s')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
state_text = ax.text(0.02, 0.9, '', transform=ax.transAxes)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, anime.animate, init_func=anime.setup,
                               frames=3000, interval=50, blit=True,repeat=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
