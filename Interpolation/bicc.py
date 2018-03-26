#!/bin/python
import numpy as np
from scipy.misc import imread, imshow
from scipy import ndimage
from scipy.interpolate import griddata
from PIL import Image,ImageEnhance
import matplotlib.pyplot as plt
def GetBicubic(imArr, posX, posY):
	out = []
	modXi = int(posX)
	modYi = int(posY)
	modXf = posX - modXi
	modYf = posY - modYi
	a = np.random.randint(0,10,10)
	sec = abs(np.cos(a * 12.0) * 10)
	#print modXi,modYi,modXf,modYf
	#sec = imArr[modXi, modYi]
	print sec
	#modXiPlusOneLim = min(modXi+1,imArr.shape[1]-1)
	#modYiPlusOneLim = min(modYi+1,imArr.shape[0]-1)
	for chan in range(imArr.shape[2]):
		pxf = pow(modXi, modXf) * pow(modYi, modYf) * sec
		#pxf = int(pxf)
		out.append(pxf)
	#print type(out)
	return out
if __name__=="__main__":
	im = imread("/Users/raghuveeramalla/Desktop/Low Resolution/batlow.jpeg")
	imShape = list(map(int, [im.shape[0]*1.6, im.shape[1]*1.6, im.shape[2]]))
	imenlarge = np.empty(imShape, dtype=np.uint8)
	#print type(imenlarge)
	print im.shape
	#rowScale = int(im.shape[0]) / int(imenlarge.shape[2])
	#colScale = int(im.shape[1]) / int(imenlarge.shape[2])
	for r in range(imenlarge.shape[2]):
		for c in range(imenlarge.shape[2]):
			#orir = r * rowScale
			#oric = c * colScale
			#imenlarge[r, c] = np.append(GetBicubic(im, oric, orir))
			np.append(imenlarge, GetBicubic(im,r,c))
	plt.imshow(im, interpolation="bicubic")
	#grid = griddata(im, imenlarge, im, method = 'cubic')
	plt.imshow(np.uint8(im))
	plt.show()
