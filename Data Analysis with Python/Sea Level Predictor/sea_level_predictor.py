import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax =plt.subplots() # Create a figure containing a single axes.
    plt.rcParams["figure.figsize"] = (25, 12)
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # MatPlotLib might work unstable with Pandas DataFrame or numpy matrix.
    # As a work around that, convert data to numpy arrays:
    year_asarray = df['Year'].values
    y2000_asarray = df.loc[(df.Year >=2000),'Year'].values # Filter out data from 2000

    first_year = df['Year'].loc[df['Year'].idxmin()]

    level_asarray = df['CSIRO Adjusted Sea Level'].values
    l2000_asarray = df.loc[(df.Year >=2000),'CSIRO Adjusted Sea Level'].values # Filter out data from 2000

    # ax.plot(year_asarray, level_asarray, label='linear')
    ax.scatter(year_asarray, level_asarray)
    
    # Create first line of best fit
    # Linear regresion curve:
    year_ext_array = range(first_year, 2050,1) # Extrapolated array till 2050
    res1 = linregress(year_asarray, level_asarray)
    print(f"From the begining R-squared: {res1.rvalue**2:.6f}")
    # ax.plot(year_asarray, res.intercept +res.slope*year_asarray, 'r')
    ax.plot(year_ext_array, res1.intercept +res1.slope*year_ext_array, 'r')


    # Create second line of best fit
    res2 = linregress(y2000_asarray, l2000_asarray)
    print(f"From the begining R-squared: {res2.rvalue**2:.6f}")
    year_ext_array2 = range(2000, 2050,1) # Extrapolated array from 2000 to 2050
    ax.plot(year_ext_array2, res2.intercept +res2.slope*year_ext_array2, 'r')

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
