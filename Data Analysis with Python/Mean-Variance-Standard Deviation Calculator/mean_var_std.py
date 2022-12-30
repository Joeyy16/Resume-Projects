"""
This code defines a function calculate that takes in a list of nine numbers and calculates the mean, variance, standard deviation, maximum, minimum, and sum of the values in the list. It also calculates these values across the rows, columns, and the entire list.

First, the function checks if the length of the input list is less than 9. If it is, it raises a ValueError with the message 'List must contain nine numbers.'. If the length of the list is 9 or greater, the function proceeds to initialize a dictionary called calculations with empty strings as the values for the keys 'mean', 'variance', 'standard deviation', 'max', 'min', and 'sum'.

Next, the function converts the input list into a 3x3 NumPy array called storage and calculates several statistics for this array, including the minimum, maximum, sum, mean, variance, and standard deviation. It also calculates these statistics for the rows, columns, and the entire array. Finally, it updates the calculations dictionary with the values for each of these statistics.

The function returns the calculations dictionary at the end.
"""

import numpy as np

def calculate(list):
    if len(list) <9:
        raise ValueError('List must contain nine numbers.')
    else:
        
        # initializing dictionary:
        calculations = {'mean' : '', 'variance' : '', 'standard deviation' : '', 'max' : '', 'min' : '', 'sum' : ''}  
    
        # Values for flattened matrix
        storage = np.array([list[0:3], list[3:6], list[6:9]])
        storage_min = storage.min()
        storage_max = storage.max()
        storage_sum = storage.sum()
        storage_mean = storage.mean()
        storage_var = storage.var()
        storage_std = storage.std()
    
        # values across the rows
        storage_min_row = storage.min(0)
        storage_max_row = storage.max(0)
        storage_sum_row = storage.sum(0)
        storage_mean_row = storage.mean(0)
        storage_var_row = storage.var(0)
        storage_std_row = storage.std(0)
    
         # values across the column
        storage_min_col = storage.min(1)
        storage_max_col = storage.max(1)
        storage_sum_col = storage.sum(1)
        storage_mean_col = storage.mean(1)
        storage_var_col = storage.var(1)
        storage_std_col = storage.std(1)
    
        # update dictionary
        # .tolist() converts numpy array to python list
        calculations.update({"min": [storage_min_row.tolist(), storage_min_col.tolist(), storage_min]})
        calculations.update({"max": [storage_max_row.tolist(), storage_max_col.tolist(), storage_max]})
        calculations.update({"sum": [storage_sum_row.tolist(), storage_sum_col.tolist(), storage_sum]})
        calculations.update({"mean": [storage_mean_row.tolist(), storage_mean_col.tolist(), storage_mean]})
        calculations.update({"variance": [storage_var_row.tolist(), storage_var_col.tolist(), storage_var]})
        calculations.update({"standard deviation": [storage_std_row.tolist(), storage_std_col.tolist(), storage_std]})




    return calculations
