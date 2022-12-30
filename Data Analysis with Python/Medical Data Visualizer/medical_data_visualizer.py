"""
This code imports four libraries: pandas, seaborn, matplotlib, and numpy.

pandas is a library for data manipulation and analysis. It provides tools to read and write data to and from various file formats, and to perform operations on the data.

seaborn is a library for statistical data visualization. It is based on matplotlib, and provides higher-level interfaces for drawing attractive and informative statistical graphics.

matplotlib is a library for data visualization. It provides functions to create a wide variety of graphs and plots, including line plots, scatter plots, bar plots, and pie charts.

numpy is a library for numerical computing. It provides tools for working with arrays and matrices of numerical data, and for performing mathematical operations on them.

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

"""
This code is reading in a CSV file called "medical_examination.csv" using the pandas library and storing the data in a DataFrame called df. It then creates a new column called 'overweight' in the DataFrame. The new column contains a value of 1 if the value in the 'weight' column divided by the square of the value in the 'height' column (both converted to meters) is greater than or equal to 25, and 0 otherwise. The numpy library's where() function is used to create the new column based on this condition.

"""

# Import data
df = pd.read_csv("medical_examination.csv")
# Add 'overweight' column
df['overweight'] = np.where(df['weight'] / (df['height'] / 100) ** 2 >= 25, 1,0)

"""
The code above is defining a new column in the df dataframe called "cholesterol" and "gluc", respectively. The values in these columns are either 0 or 1, depending on the value in the corresponding column of the original dataframe. If the value in the original dataframe is 1, the new value is 0, and vice versa. This code is using the np.where() function, which takes a condition as the first argument and two values as the second and third arguments. If the condition is True, the function returns the second argument, and if the condition is False, it returns the third argument. In this case, the condition is df["cholesterol"] == 1 or df["gluc"] == 1, and the values returned are 0 and 1, respectively.
"""

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)
df["gluc"] = np.where(df["gluc"] == 1, 0, 1)

"""
The code above defines a function called draw_cat_plot() which creates a bar plot using the sns.catplot() function from the seaborn library. The plot displays the counts of different features in the original dataframe, such as cholesterol levels, glucose levels, and smoking status, split by the values of the cardio column.

The function starts by creating a new dataframe called df_cat using the pd.melt() function. This function converts the dataframe into a 'long' format, where each row represents a unique id-variable combination. In this case, the id_vars parameter specifies that the cardio column should be used as the id variables, and the value_vars parameter specifies the columns to use as value variables.

Next, the function groups the data in df_cat by the cardio, variable, and value columns, and counts the number of rows in each group using the size() method. It then resets the index and renames the column containing the counts to total.

Finally, the function calls the sns.catplot() function and passes in the data from df_cat as the data parameter. The x parameter specifies the column to use as the x-axis labels, the y parameter specifies the column to use as the y-axis values, and the hue parameter specifies the column to use to group the data. The col parameter specifies a column to split the data into subplots, and the kind parameter specifies the type of plot to use (in this case, a bar plot).

The function saves the plot to an image file called catplot.png and returns the figure object.

"""

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = "cardio", value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight','cardio'])

    df_cat = df_cat.groupby(["cardio","variable","value"]).size().reset_index().rename(columns={0:"total"})  
  
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    # Draw the catplot with 'sns.catplot()'
    plots = sns.catplot(x="variable", y="total", hue="value", col = "cardio", kind="bar", data=df_cat)
    fig = plots.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

"""
The code above defines a function called draw_heat_map that generates a heat map showing the correlation between different variables in a dataset. The function first filters the data by removing rows that don't meet certain conditions: the systolic blood pressure must be less than or equal to the diastolic blood pressure, the height must be within the 2.5th and 97.5th percentiles, and the weight must also be within the 2.5th and 97.5th percentiles. Then, the function calculates the correlation matrix for the filtered data using the corr() method. The function creates a mask for the upper triangle of the matrix, which is set to True for all elements above the diagonal and False for all elements below the diagonal. The function then uses sns.heatmap() to draw the heat map and saves it to an image file called 'heatmap.png'. The function returns the figure object created by sns.heatmap().

"""


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    pressure_condition = df['ap_lo'] <= df['ap_hi']

    height_condition = np.logical_and(df['height'] >= df['height'].quantile(0.025), df['height'] <= df['height'].quantile(0.975))

    weight_condition = np.logical_and(df['weight'] >= df['weight'].quantile(0.025), df['weight'] <= df['weight'].quantile(0.975))

    df_heat = df.loc[pressure_condition & height_condition & weight_condition]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype = bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig = plt.figure(figsize = (14,8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, annot = True, fmt=".1f" )

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

