#!/bin/python
import numpy as np
from scipy.misc import imread, imshow
from scipy import ndimage
from PIL import Image,ImageEnhance
import matplotlib.pyplot as plt
def GetBilinearPixel(imArr, posX, posY): # all the computation is done here
	out = [] #the output pixel value is stored here
	modXi = int(posX) #decimal value is removed for later computation
	modYi = int(posY)
	modXf = posX - modXi #difference in decimal
	modYf = posY - modYi
	modXiPlusOneLim = min(modXi+1,imArr.shape[1]-1) # x value limit
	modYiPlusOneLim = min(modYi+1,imArr.shape[0]-1) # y value limit
	for chan in range(imArr.shape[2]):
		bl = imArr[modYi, modXi, chan] #intialization
		br = imArr[modYi, modXiPlusOneLim, chan]
		tl = imArr[modYiPlusOneLim, modXi, chan]
		tr = imArr[modYiPlusOneLim, modXiPlusOneLim, chan]
		b = modXf * br + (1. - modXf) * bl
		t = modXf * tr + (1. - modXf) * tl
		pxf = modYf * t + (1. - modYf) * b
		out.append(int(pxf+0.5)) #pixel value in 1X3 form is sent
	return out
if __name__=="__main__": #main
	im = imread("/Users/raghuveeramalla/Desktop/Low Resolution/batlow.jpeg")
	print im
	imShape = list(map(int, [im.shape[0]*0.5, im.shape[1]*0.5, im.shape[2]])) #convertion of image into list
	imenlarge = np.empty(imShape, dtype=np.uint8) #non empty intialization
	rowScale = float(im.shape[0]) / float(imenlarge.shape[0]) #row weights
	colScale = float(im.shape[1]) / float(imenlarge.shape[1]) #column weights
	for r in range(imenlarge.shape[0]):
		for c in range(imenlarge.shape[1]):
			orir = r * rowScale
			oric = c * colScale
			imenlarge[r, c] = GetBilinearPixel(im, oric, orir)
blurred_f = ndimage.gaussian_filter(imenlarge, 0.05) #to add gaussian filters
filter_blurred_f = ndimage.gaussian_filter(blurred_f, 0.25) #still filtering
alpha = 3  #filters used
sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f) #sharpening the processed image
sharpened2=sharpened + alpha * (blurred_f - filter_blurred_f) #sharpening the sharpened image
#plt.imshow(im, interpolation="bicubic")
#plt.show()
#plt.imshow(im, interpolation="nearest")
#plt.show()
plt.imshow(np.uint8(sharpened)) #how to display the image
plt.show()
