import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
print "######################## 2D simulation ################"

# initialization function: plot the background of each frame
class IVER(object):
    def __init__(self):
        self.speed=5000.0
        self.operation_time=6.0
        self.operation_distance=self.operation_time*self.speed
        self.battery=1.0
        self.start_x=0.0
        self.start_y=0.0
        self.position_x=0.0
        self.position_y=0.0
        self.history_x=[]
        self.history_y=[]
        self.recharging=False
        self.motion_width=4000.0
        self.motion_forward_step=150.0
        self.forward=False
        self.right=False
        self.recharge_time=3.5
        self.number_of_recharges=0
        self.number_of_forward_steps=0

    def positionEstimation(self,number_of_recharges,life):
        path_length=life*self.operation_distance+number_of_recharges*self.operation_distance
        position_calculation_x=self.position_x
        position_calculation_y=self.position_y
        forward=self.forward
        right=self.right
        change_right=False
        change_forward=False
        while path_length>0:
            
            # print "right",right
            if forward:
                # print "forward"
                remaining_x=(self.number_of_forward_steps+1)*self.motion_forward_step-position_calculation_x
                if path_length>remaining_x:
                    # print "forward is long"
                    change_forward=True 
                    self.number_of_forward_steps+=1
                    position_calculation_x+=remaining_x
                    path_length-=remaining_x
                else:
                    position_calculation_x+=path_length
                    path_length=0 
                
            else:
                
                if right:
                    # print "right"
                    if path_length>position_calculation_y:
                        change_forward=True
                        change_right=True
                        path_length-=position_calculation_y
                        position_calculation_y=0
                    else:
                        position_calculation_y-=path_length
                        path_length=0
                else:
                    # print "left"
                    if path_length>self.motion_width-position_calculation_y:
                        change_forward=True
                        change_right=True
                        path_length=path_length-(self.motion_width-position_calculation_y)
                        position_calculation_y=self.motion_width
                    else:
                        position_calculation_y+=path_length
                        path_length=0
            if change_forward:
                forward=not forward
                change_forward=False
            if change_right:
                right=not right
                change_right=False
        return position_calculation_x,position_calculation_y,forward,right

    def timeEstimation(self,number_of_recharges):
        time=self.operation_time*(number_of_recharges+1)+number_of_recharges*self.recharge_time
        return time

    def animationStep(self,time_step):
        battery_step=time_step/self.operation_time
        battery_step=min(battery_step,self.battery)
        self.battery-=battery_step
        if self.battery<=0:
            self.recharging=True
            # battery_step=0
        self.position_x,self.position_y,self.forward,self.right=self.positionEstimation(0,battery_step)
        self.history_x.append(self.position_x)
        self.history_y.append(self.position_y)
        return self.position_x,self.position_y

    def recharge(self,time_step):
        battery_step=time_step/self.recharge_time
        self.battery+=battery_step
        if self.battery>1:
            self.recharging=False
            self.battery=1

class GLIDER(object):
    def __init__(self,x=0,y=0):
        self.speed=100.0
        self.battery=1.0
        self.deploy_time=0
        self.travel_time=0
        self.stop_time=0
        self.position_x=1000
        self.position_y=2000
        self.history_x=[]
        self.history_y=[]
        self.target_x=x
        self.target_y=y
        self.theta=0

    def calculateTimes(self):
        distance=np.sqrt((self.position_x-self.target_x)**2+(self.position_y-self.target_y)**2)
        self.travel_time=distance/self.speed
        self.deploy_time=self.stop_time-self.travel_time

    def setLocations(self,target_x,target_y):
        self.target_x=target_x
        self.target_y=target_y
        self.theta=np.arctan2(self.target_y-self.position_y,self.target_x-self.position_x)
    def animationStep(self,time_step):
        moving_step=time_step*self.speed
        distance_to_target=np.sqrt((self.target_x-self.position_x)**2+(self.target_y-self.position_y)**2)
        moving_step=min(moving_step,distance_to_target)
        self.position_x+=moving_step*np.cos(self.theta)
        self.position_y+=moving_step*np.sin(self.theta)
        self.history_x.append(self.position_x)
        self.history_y.append(self.position_y)

class ANIMATION(object):
    def __init__(self):
        self.ivers=[]
        self.gliders=[]
        self.ivers_trajectories=[]
        self.gliders_trajectories=[]
        self.simulation_start_time=0

    def addGlider(self,number):
        if len(self.ivers)<=0:
            print "Add Ivers before gliders"
            return None
        for i in range(0,number):
            self.gliders.append(GLIDER())
            target_x,target_y,_,_=self.ivers[0].positionEstimation(i,self.ivers[0].battery)
            self.gliders[i].setLocations(target_x,target_y)
            self.gliders[i].stop_time=self.ivers[0].timeEstimation(i)
            self.gliders[i].calculateTimes()
            self.simulation_start_time=min(self.simulation_start_time,self.gliders[i].deploy_time)
            self.ivers[0].number_of_forward_steps=0
            print "For glider #",i,"deploy time, travel time and stop time are",self.gliders[i].deploy_time,self.gliders[i].travel_time,self.gliders[i].stop_time
            print "target @",target_x,target_y
    def addIVER(self,number):
        for i in range(0,number):
            self.ivers.append(IVER())
            print "Made IVER"

    def setup(self):
        iver.set_data([], [])
        gliders.set_data([],[])
        for mline in iver_trajectory:
            mline.set_data([],[])
        for mline in glider_trajectory:
            mline.set_data([],[])
        time_text.set_text('')
        state_text.set_text('')
        return iver,gliders,iver_trajectory,glider_trajectory,time_text,state_text

    def animate(self,i):

        # Setup
        time_step=.1
        time=i*time_step+self.simulation_start_time
        time_text.set_text('time = %.1f hr' %time )
        gliders_position_x=[]
        gliders_position_y=[]
        ivers_position_x=[]
        ivers_position_y=[]
        max_recharge_available=1
        
        # Calculate max recharge available time
        for glider in self.gliders:
            max_recharge_available=max(max_recharge_available,glider.stop_time+self.ivers[0].recharge_time+1)
        # For IVERS
        for i in range(0,len(self.ivers)):
            if time>=0:
                if not self.ivers[i].recharging:
                    x,y=self.ivers[i].animationStep(time_step)
                else:
                    # recharge
                    if time<=max_recharge_available:
                        self.ivers[i].recharge(time_step)
                    x,y,_,_=self.ivers[i].positionEstimation(0,0)
            else:
                x,y,_,_=self.ivers[i].positionEstimation(0,0)
            ivers_position_x.append(x)
            ivers_position_y.append(y)
            self.ivers[i].history_x.append(x)
            self.ivers[i].history_y.append(y)
            iver_trajectory[i].set_data([self.ivers[i].history_x],[self.ivers[i].history_y])
            battery_bar_length=20
            battery_bar=int(self.ivers[0].battery*100)
            state_text.set_text('Battery status: %%%s' %battery_bar)

        # For GLIDERS
        for i in range(0,len(self.gliders)):
            if time>=self.gliders[i].deploy_time and time<=(self.gliders[i].stop_time):
                self.gliders[i].animationStep(time_step)
            gliders_position_x.append(self.gliders[i].position_x)
            gliders_position_y.append(self.gliders[i].position_y)
            self.gliders[i].history_x.append(self.gliders[i].position_x)
            self.gliders[i].history_y.append(self.gliders[i].position_y)
            glider_trajectory[i].set_data([self.gliders[i].history_x],[self.gliders[i].history_y])
        
        # Return results
        iver.set_data(ivers_position_x, ivers_position_y)
        gliders.set_data(gliders_position_x,gliders_position_y)
        return iver,gliders,iver_trajectory,glider_trajectory,time_text,state_text


anime=ANIMATION()
anime.addIVER(1)
anime.addGlider(4)


fig = plt.figure(num=None, figsize=(20, 4), dpi=80)
ax = plt.axes(xlim=(-100, 8000), ylim=(-500, anime.ivers[0].motion_width*1.2))

iver, = ax.plot([], [],'ko', lw=2,markersize=10)
gliders, = ax.plot([], [],'ro', lw=2,marker='s')
iver_trajectory =[ax.plot([], [],'k', lw=1)[0] for m in range(len(anime.ivers))]
glider_trajectory =[ax.plot([], [],'r', lw=1)[0] for n in range(len(anime.gliders))]
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
state_text = ax.text(0.02, 0.9, '', transform=ax.transAxes)
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, anime.animate, init_func=anime.setup,
                               frames=20000,interval=2,repeat=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
