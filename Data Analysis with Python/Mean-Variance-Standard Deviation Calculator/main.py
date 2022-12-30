"""
This code is printing the result of the calculate() function when it is passed a list of integers as an argument. The calculate() function is defined in the mean_var_std module and it is used to calculate the mean, variance, and standard deviation of a list of numbers. When this code is executed, it will print a tuple containing the mean, variance, and standard deviation of the list of integers passed to the calculate() function.

"""

# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
