import numpy as np
from scipy.misc import imread, imshow
from scipy import ndimage
from PIL import Image,ImageEnhance
import matplotlib.pyplot as plt
def nearest_neighbor(x,y,v,grid):
    for i in xrange(grid.shape[2]):
        for j in xrange(grid.shape[0]):
            distance = np.sqrt((x-i)**2+(y-j)**2)
            grid[i,j] = v[distance.argmin()]
    return grid
if __name__=="__main__":
	im = imread("/Users/raghuveeramalla/Desktop/Low Resolution/batlow.jpeg")
	#np.random.seed(123)
	#grid = np.zeros((100,100),dtype='uint8')
	x,y = np.random.randint(0,100,10),np.random.randint(0,100,10)
	v = np.random.randint(0,10,10)
	imenlarge = nearest_neighbor(x,y,v,im)
	plt.imshow(np.uint8(imenlarge))
	plt.show()
    
