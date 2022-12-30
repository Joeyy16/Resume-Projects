"""
The code above is importing several libraries that will be used in the subsequent code. The matplotlib library is a 2D plotting library that allows users to create line plots, scatter plots, bar plots, error bars, etc. The pandas library is a data manipulation and analysis library that provides functions for reading and writing data, filtering and grouping data, and performing statistical analyses. The seaborn library is a data visualization library that is built on top of matplotlib and provides additional functionality for creating statistical plots. The calendar library provides functions for working with dates and times. The register_matplotlib_converters function from the pandas.plotting module is used to register pandas' date converters with matplotlib, which allows matplotlib to correctly handle dates when creating plots.

"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar
register_matplotlib_converters()

"""
The code above is reading in data from a csv file called "fcc-forum-pageviews.csv" using the pandas read_csv() function and storing it in a dataframe called df. It then converts the 'date' column in the dataframe to a datetime data type using the astype() function. Finally, it sets the 'date' column as the index of the dataframe using the set_index() function. This allows the dataframe to be indexed by date, which can be useful for time series analysis.

"""

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df['date']= df['date'].astype('datetime64[ns]')
df = df.set_index("date")

"""
The code above is filtering the rows in the "df" dataframe by selecting only those rows whose value in the "value" column is greater than or equal to the 2.5th percentile of the "value" column and less than or equal to the 97.5th percentile of the "value" column. This is being done using the & operator to combine the two conditions, which checks for the presence of both conditions. The .quantile() method returns the specified percentile of the data in a series, in this case the "value" column of the "df" dataframe. The resulting dataframe will contain rows with values in the "value" column that are within the specified range.

"""

# Clean data
df = df[(df["value"]>= df["value"].quantile(0.025)) & (df["value"]<= df["value"].quantile(0.975))]

"""
The code above defines a function called "draw_line_plot()" that creates a line plot using matplotlib. The plot shows the daily page views of the freeCodeCamp forum from May 2016 to December 2019. The x-axis represents the dates, which are taken from the "date" column of the df dataframe and set as the index. The y-axis represents the page views, which are taken from the "value" column of the df dataframe. The plot is labeled with a title and x- and y-axis labels. The function then saves the plot as an image file and returns the figure object.

"""

def draw_line_plot():
    # Draw line plot
    
    fig, ax = plt.subplots(figsize=(20, 6))

    ax = plt.plot(df.index, df['value'])

    plt.ylabel("Page Views")
    plt.xlabel("Date")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

"""
The function draw_bar_plot() creates a bar plot showing the average page views for each month over a period of years. It does this by first copying the original data and creating new columns for the year and month of each row. It then groups the data by year and month and calculates the mean page views for each group. The resulting data is reshaped so that each year becomes a row and each month becomes a column, with the average page views for that month and year as the value in each cell. The resulting data is then plotted using the plot.bar() method of a Pandas DataFrame. The x-axis is labeled "Years" and the y-axis is labeled "Average Page Views", and a legend is added with the title "Months". The resulting plot is saved to an image file and the figure object is returned.
"""

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)


    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(["year","month"])['value'].mean().reset_index().sort_values(by=['year','month'])
    df_bar = df_bar.set_index('year')
    df_bar = df_bar.pivot_table(values = "value", index=df_bar.index, columns="month", aggfunc='first').reset_index()

    df_bar = df_bar.set_index('year')
    df_bar.columns = ['January','February','March','April','May','June','July','August','September','October','November','December']
    df_bar= df_bar.fillna(0)
    

    fig, ax = plt.subplots()

    bar = df_bar.plot.bar(rot=0, ax=ax)
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

"""
The draw_box_plot function generates two box plots using the Seaborn library. The first box plot is a year-wise box plot that shows the trend in page views over the years. The second box plot is a month-wise box plot that shows the seasonality in page views over the months.

The function first makes a copy of the data and resets the index, adding a "year" column with the year of each date and a "month" column with the month of each date. It then creates two subplots in a figure and uses the Seaborn boxplot function to draw the box plots on these subplots. The first box plot is drawn using the "year" column for the x-axis and the "value" column for the y-axis. The second box plot is drawn using the "month" column for the x-axis and the "value" column for the y-axis. The function sets the x-axis labels, y-axis labels, and titles for the two subplots and saves the figure as an image. It then returns the figure object.
"""

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_figheight(15)
    fig.set_figwidth(60)


    sns.boxplot(ax=ax1, x="year", y= "value", data=df_box) 
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    sns.boxplot(ax=ax2, x="month", y= "value", data=df_box, order = month_order) 
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
