import numpy as np
from scipy.misc import imread
import scipy.stats
if __name__=="__main__":
    im = imread("/Users/raghuveeramalla/Desktop/83.jpg")
    im2 = imread("/Users/raghuveeramalla/Desktop/82.jpg")
    im3 = imread("/Users/raghuveeramalla/Desktop/80.jpg")
    im4 = imread("/Users/raghuveeramalla/Desktop/81.jpg")
    #snr = stats.mstats.sem(im,axis = None,ddof = 0)
    #print snr
    print "Actual output"
    snr = scipy.stats.signaltonoise(im2,axis = None)
    print snr
    print "Expected output"
    snr = scipy.stats.signaltonoise(im4,axis = None)
    print snr
