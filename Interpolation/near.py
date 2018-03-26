from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
def nearest_neighbor(x,y,v,grid):
    for i in xrange(grid.shape[0]):
        for j in xrange(grid.shape[1]):
            distance = np.sqrt((x-i)**2+(y-j)**2)
            grid[i,j] = v[distance.argmin()]
    return grid

np.random.seed(123433789)
grid = np.zeros((100,100),dtype='uint8')
x,y = np.random.randint(0,100,10),np.random.randint(0,100,10)
v = np.random.randint(0,10,10) 

grid = nearest_neighbor(x,y,v,grid)
plt.imshow(grid.T,origin='lower',interpolation='nearest',cmap='jet')
plt.scatter(x,y,c=v,cmap='jet',s=120)
plt.xlim(0,grid.shape[0])
plt.ylim(0,grid.shape[1])
plt.grid()
plt.show()
