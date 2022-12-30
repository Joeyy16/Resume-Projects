
"""
The function calculate_demographic_data in the module demographic_data_analyzer calculates various statistical values for a given dataset of demographic data. The dataset is a list of dictionaries, where each dictionary represents the demographic data for an individual. The statistical values that the function calculates include the mean, median, mode, and standard deviation for the following data points:

Age
Income
Household Size
The function returns a dictionary with keys for each of these data points, and the corresponding value is another dictionary with keys for the statistical values (mean, median, mode, and standard deviation) and their corresponding values.

For example, if the input data looks like this:

[
{'age': 35, 'income': 55000, 'household_size': 1},
{'age': 42, 'income': 60000, 'household_size': 3},
{'age': 30, 'income': 65000, 'household_size': 2},
{'age': 35, 'income': 70000, 'household_size': 1},
{'age': 60, 'income': 80000, 'household_size': 2},
]

Then the function might return a dictionary like this:

{
'age': {'mean': 41.0, 'median': 35.0, 'mode': 35, 'standard deviation': 14.7},
'income': {'mean': 66500.0, 'median': 62500.0, 'mode': 70000, 'standard deviation': 5500.0},
'household_size': {'mean': 1.6, 'median': 2.0, 'mode': 1, 'standard deviation': 0.8},
}
"""

# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

