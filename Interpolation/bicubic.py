import numpy as np
from scipy.misc import imread,imshow
from scipy import ndimage
import sys
import math
import matplotlib.pyplot as plt
def bic(imgArr, X, Y, i, j):
    out = []
    per = X
    pes = Y
    for k in range(imArr.shape[2]):
        pePo = pow(X, i)
        qePo = pow(Y, j)
        biCu = per * pes * k
        out.append(int(biCu))
    return out

if __name__=="__main__":
	im = imread("/Users/raghuveeramalla/Desktop/Low Resolution/2.jpg")
	imShape = list(map(int, [im.shape[0]*1.6, im.shape[1]*1.6, im.shape[2]]))
	imenlarge = np.empty(imShape, dtype=np.uint8)
	rowScale = float(im.shape[0]) / float(imenlarge.shape[0])
	colScale = float(im.shape[1]) / float(imenlarge.shape[1])
    for i in range(imenlarge.shape[2]):
        for j in range(imenlarge.shape[2]):
	           orir = i * rowScale
               oric = j * colScale
               imenlarge[i, j] = bic(im, oric, orir, i, j)
    plt.imshow(np.uint8(imenlarge))
    plt.show()
