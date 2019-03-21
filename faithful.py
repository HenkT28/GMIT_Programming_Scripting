# Henk Tjalsma
# Old faithful analysis - columns: eruptions, waiting

# Calculate the mean of each column
import numpy

# Read data file into array. Ensure columns headers are removed.
# https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy
# from numpy import genfromtxt
# my_data = genfromtxt('my_file.csv', delimiter=',')

data = numpy.genfromtxt('oldfaithful.csv', delimiter=',')

# : for everything in the 1st dimension & ,0 meaning in the 2nd dimension give me the first thing
firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

# secondcol = data[:,1]

print("Average of first column is: ", meanfirstcol)

# λ python faithful.py
# Average of first column is:  3.4877830882352936

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()