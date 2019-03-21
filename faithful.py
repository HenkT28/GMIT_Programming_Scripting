# Henk Tjalsma
# Old faithful analysis - columns: eruptions, waiting

# Calculate the mean of each column
import numpy

# Read data file into array. Ensure columns headers are removed.
data = numpy.genfromtxt('oldfaithful.csv', delimiter=',')

firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

print("Average of first column is: ", meanfirstcol)

# λ python faithful.py
# Average of first column is:  3.4877830882352936

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()