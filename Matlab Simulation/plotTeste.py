import matplotlib.pyplot as plt
import numpy
from scipy import *

t=100
y=[]
x=[]

for step in range(t):
	value=step*2*pi/t
	value=value**2+3*value-30
	y.append(cos(value))
	value=value+40*value-30
	x.append(sin(value))

fig = plt.figure()
ax=fig.gca()
ax.plot(x,y)
plt.show()