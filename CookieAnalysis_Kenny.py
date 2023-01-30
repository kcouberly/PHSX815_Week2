#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    
    #dividing the times into quantiles of equal size 
    
    #adding argument to file (default 4 if no arg)
    if '-quant' in sys.argv:
        p = sys.argv.index('-quant')
        N = int(sys.argv[p+1])
    else:
        N = 4
    A = len(times)
    B = math.floor(A/N)
    #fills array with the cutoff values for each quantile
    quantiles = []
    for x in range(A):
        #start at 1 to get end points instead of start points
        if (x+1)%B == 0:
            quantiles.append(times[x])
    
    #plotting distribution of times as a histogram
    n, bins, patches = plt.hist(times, 5, facecolor='g', alpha=0.75)
    
    plt.xlabel('Time')
    plt.ylabel('Number of Events')
    plt.title('Histogram of Cookie Times')
    plt.grid(True)
    plt.show()
    
    #pie plot of quantiles
    labels = []
    for x in range(len(quantiles)):
        labels.append(str(x+1))
    plt.pie(quantiles,labels=labels)
    plt.title('Quantiles')
    plt.show()
    times_avg = Sorter.DefaultSort(times_avg)
