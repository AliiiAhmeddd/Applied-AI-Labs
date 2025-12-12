#Antesar Lab Tasks

#Lab 1
# Exercise 1: We have registered the speed of 13 cars:
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# Write a Python program to calculate the average, the middle, or the most common speed value?

# The Python code for the calculation of mean, median, and mode using a numpy array and the stats package (look at last cell to review the Python AI libraries) is as follows:

import numpy as np
from scipy import stats

# data would be provided as a one-dimensional array
data = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# Calculate Mean
dt_mean = np.mean(data) ; print ("Mean :",round(dt_mean,2))

# Calculate Median
dt_median = np.median(data) ; print ("Median :",dt_median)

# Calculate Mode
dt_mode =  stats.mode(data); print ("Mode :",dt_mode[0])

# Exercise 2: Let's say we have an array of the ages of all the people that lives in a street.
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# What is the 75. percentile? What does it mean?
# Write a Python code that calculate what is the age that 90% of the people are younger than?

#75th percentile means the value below which 75% of the people’s ages fall
#Python code for 75th Percentile 

import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentile_75 = np.percentile(ages, 75)
print("75th percentile age is:", percentile_75)

#Pyhton Code to find the age that 90% of the people are younger than

percentile_90 = np.percentile(ages, 90)
print("90% of people are younger than age:", percentile_90)
