import numpy as np
from scipy.misc import imread, imshow
from scipy import stats
import sys
import math
def psnr(target,ref):
    target_data = np.array(target,dtype=np.float64)
    ref_data = np.array(ref,dtype=np.float64)
    diff = ref_data - target_data
    print(diff.shape)
    diff = diff.flatten('C')
    rmse = math.sqrt(np.mean(diff ** 2.))
    return 20 * math.log10(255 / rmse)
if __name__=="__main__":
    im = imread("/Users/raghuveeramalla/Desktop/80.jpg")
    im1 = imread("/Users/raghuveeramalla/Desktop/81.jpg")
    #im2 = imread("/Users/raghuveeramalla/Desktop/33.png")
    #im3 = imread("/Users/raghuveeramalla/Desktop/34.png")
    #im4 = imread("/Users/raghuveeramalla/Desktop/30.jpg")
    #im5 = imread("/Users/raghuveeramalla/Desktop/301.jpg")
    print(psnr(im,im1) * pow(10, -2))

