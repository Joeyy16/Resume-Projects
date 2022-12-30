"""
These lines of code import the necessary libraries and modules that will be used in the script.

The pandas library is a powerful library for data manipulation and analysis in Python. It is used to import and manipulate the data stored in the .csv file.

The matplotlib.pyplot library is a plotting library used for creating various types of plots in Python. It is used to create a line plot of the sea level data.

The linregress function from the scipy.stats library is used to perform a linear regression on the sea level data and obtain the slope and intercept values for the regression line. This will be used to make predictions about future sea level values.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

"""
The code above is reading in a CSV file called 'epa-sea-level.csv' using the read_csv function from the pandas library. This function reads in the data from the file and stores it in a dataframe called 'df'. The data in this file contains information about sea level measurements over time.
"""

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    """
    The code above is creating a figure object and an axis object using the plt.subplots() function. The plt.rcParams["figure.figsize"] line sets the size of the figure to be 25 inches wide and 12 inches tall. The ax.set_title(), ax.set_xlabel(), and ax.set_ylabel() lines are setting the title, x-axis label, and y-axis label of the plot, respectively. These labels will be displayed on the plot when it is shown.

    """

    # Create scatter plot
    fig, ax =plt.subplots() # Create a figure containing a single axes.
    plt.rcParams["figure.figsize"] = (25, 12)
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    """
    The code above is creating arrays of values from the 'Year' and 'CSIRO Adjusted Sea Level' columns of the df dataframe. It is also creating two new arrays that only contain values from the 'Year' and 'CSIRO Adjusted Sea Level' columns for rows where the 'Year' value is greater than or equal to 2000. It is also finding the minimum value in the 'Year' column and saving it in the variable 'first_year'. These arrays will be used later for plotting and performing a linear regression analysis.

    """

    # MatPlotLib might work unstable with Pandas DataFrame or numpy matrix.
    # As a work around that, convert data to numpy arrays:
    year_asarray = df['Year'].values
    y2000_asarray = df.loc[(df.Year >=2000),'Year'].values # Filter out data from 2000

    first_year = df['Year'].loc[df['Year'].idxmin()]

    level_asarray = df['CSIRO Adjusted Sea Level'].values
    l2000_asarray = df.loc[(df.Year >=2000),'CSIRO Adjusted Sea Level'].values # Filter out data from 2000
    
    """
    The code above is creating a scatter plot on the "ax" Axes object. The x-axis of the plot is being set to the values in the "year_asarray" array, and the y-axis is being set to the values in the "level_asarray" array. This will create a scatter plot with one point for each year in "year_asarray" and the corresponding sea level value in "level_asarray".

    """

    # ax.plot(year_asarray, level_asarray, label='linear')
    ax.scatter(year_asarray, level_asarray)
    
    """
    The code above is plotting a scatter plot of the 'Year' and 'CSIRO Adjusted Sea Level' columns of the df dataframe on the 'ax' axes object. Then, it is creating an array called 'year_ext_array' that goes from the minimum year in the 'Year' column of df to 2050 in steps of 1. This array will be used to extrapolate the data beyond the range of the original data. The code then performs a linear regression on the 'Year' and 'CSIRO Adjusted Sea Level' columns of the df dataframe and prints the R-squared value of the regression. Finally, it plots the extrapolated data using the 'ax.plot()' function and the 'year_ext_array' array, with the slope and intercept of the linear regression as the parameters.
    
    """
    
    # Create first line of best fit
    # Linear regresion curve:
    year_ext_array = range(first_year, 2050,1) # Extrapolated array till 2050
    res1 = linregress(year_asarray, level_asarray)
    print(f"From the begining R-squared: {res1.rvalue**2:.6f}")
    # ax.plot(year_asarray, res.intercept +res.slope*year_asarray, 'r')
    ax.plot(year_ext_array, res1.intercept +res1.slope*year_ext_array, 'r')


    """
    The code above is using the linregress function from the scipy.stats module to perform linear regression on two sets of data: the sea level data from the beginning of the dataset, and the sea level data from the year 2000 onwards. Linear regression is a statistical method used to model the linear relationship between two variables, in this case, the year and the sea level. The linregress function returns several values, including the slope and intercept of the regression line, as well as the correlation coefficient (rvalue).

    The code then creates two sets of extrapolated data, one from the first year in the dataset to the year 2050, and another from the year 2000 to the year 2050. These extrapolated data are used to plot the regression lines on the scatterplot using the plot function. The rvalue**2 value is also printed out, which is the squared correlation coefficient, also known as the coefficient of determination. This value represents the proportion of the variance in the dependent variable that is predictable from the independent variable. A value close to 1 indicates a strong linear relationship between the two variables.
    """
    
    # Create second line of best fit
    res2 = linregress(y2000_asarray, l2000_asarray)
    print(f"From the begining R-squared: {res2.rvalue**2:.6f}")
    year_ext_array2 = range(2000, 2050,1) # Extrapolated array from 2000 to 2050
    ax.plot(year_ext_array2, res2.intercept +res2.slope*year_ext_array2, 'r')

    # Add labels and title

    """
    The code above is defining a function called draw_plot which is used to create a plot showing the rise in sea level over time. It reads in data from a CSV file and creates a scatter plot of the data using ax.scatter(). It then uses the linregress() function from the scipy.stats module to fit a linear regression model to the data and calculates the R-squared value for the model. The function then plots two lines on the same plot using ax.plot(), one representing the linear regression model fit to all the data and another representing the linear regression model fit to data from the year 2000 onwards. Finally, the function saves the plot as an image and returns the Axes object containing the plot.
    """
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
