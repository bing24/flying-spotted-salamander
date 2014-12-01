import matplotlib.pyplot as plt
import numpy as np
from scipy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

length=40;
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.auto_scale_xyz([-length,length], [-length,3*length], [0,2*length])

# base=np.zeros((length,length))
# base

# for(x in range(0,length))
# 	for(y in range(0,length))
# 		base[x,y]=exp(-(x**2+y**2)/2)/sqrt(2*pi)

x = np.arange(-length, length, .5)
y=x
xx, yy = meshgrid(x, y, sparse=True)
var=round(length/3);
z=exp(-(xx**2+yy**2)/(2*var**2))/(sqrt(2*pi)*var)
size(z)
h = cset = ax.contour(x,y,z, cmap=cm.cool)
surf = ax.plot_wireframe(xx, yy, z, rstride=1, cstride=1, cmap=cm.cool,
        linewidth=0.05, antialiased=True)
ax.auto_scale_xyz([-length,length], [-length,length], [0,2*z.max()])
plt.show()
