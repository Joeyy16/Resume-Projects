"""
Pandas is a software library in Python for data manipulation and analysis. It is built on top of the NumPy library and allows for fast analysis 
and data cleaning and preparation. It provides easy-to-use data structures and data analysis tools for handling and manipulating large amounts of 
data. The pd abbreviation is a commonly used alias for the pandas library. It is used to import the library into the current namespace, so that you 
can use the functions and methods provided by pandas without having to prefix them with pandas.
"""

import pandas as pd

"""
This code reads in a CSV file called 'adult.data.csv' using the read_csv function from the pandas library. The read_csv function returns a DataFrame
object which is a 2-dimensional size-mutable tabular data structure with rows and columns. The head() method is then called on the DataFrame object, 
which returns the first 5 rows of the data as a preview. This can be useful for getting a feel for the structure and contents of the data.
"""

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head()
    
    """
    The race_count variable is a pandas.core.series.Series object that contains the counts of unique values in the race column of the df dataframe. The value_counts() method returns a series containing counts of unique values. The resulting race_count series is indexed by the unique values in the race column and has values equal to the counts of those values in the column. For example, if the race column contained the values ["White", "White", "Black", "Asian"], the resulting race_count series would be {"White": 2, "Black": 1, "Asian": 1}.
    """

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    """
    The code creates a filter to select only the rows where the 'sex' column is 'Male' and stores this in the variable 'filter1'. It then uses the '.where()' method on the 'age' column of the dataframe, passing in the filter as an argument, to create a new dataframe 'df_male_age' that only includes the rows where the 'sex' column is 'Male' and the values in the 'age' column. Finally, it calculates the average of the values in the 'age' column of this new dataframe using the '.mean()' method and rounds it to one decimal place using the 'round()' function. The resulting value is stored in the variable 'average_age_men'.
    """

    # What is the average age of men?
    filter1 = df['sex'] == 'Male'
    df_male_age = df['age'].where(filter1)
    average_age_men = round(float(df_male_age.mean()),1)
    
    """
    This code is calculating the percentage of individuals in the df dataframe who have a "Bachelors" degree. It does this by first creating a filter filter2 which selects rows where the education column is equal to "Bachelors". Then, it applies this filter to the education column using the where() method, and drops any null values using the dropna() method. It then counts the number of non-null values in the resulting series using the count() method, and divides this value by the total number of rows in the education column. Finally, it multiplies this value by 100 and rounds it to one decimal place to get the percentage of individuals with a "Bachelors" degree.
    """

    # What is the percentage of people who have a Bachelor's degree?
    filter2 = df['education'] == 'Bachelors'
    suma2 = df['education'].where(filter2).dropna().count()
    percentage_bachelors = round((suma2 / df['education'].count()) * 100,1)
    
    """
    This code defines three filters that are used to select rows from the dataframe df. The first filter, filter3, selects rows where the value in the 'salary' column is '>50K'. The second filter, filter3a, selects rows where the value in the 'education' column is 'Bachelors', 'Masters', or 'Doctorate'. The third filter, filter3b, selects rows where the value in the 'education' column is not 'Bachelors', 'Masters', or 'Doctorate'. These filters are not applied to the dataframe yet, they are just defined.
    """

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    filter3 = df['salary'] == '>50K' 
    
    filter3a = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    
    filter3b = ~(df['education'] == 'Bachelors') & ~(df['education'] == 'Masters') & ~(df['education'] == 'Doctorate')
    
    """
    The code is creating two variables, higher_education and lower_education, which represent the number of rows in the education column of the df dataframe that satisfy certain conditions.

    For higher_education, the condition is that the value in the education column is either "Bachelors", "Masters", or "Doctorate". This condition is represented by the filter3a variable, which is created by using the logical | operator (meaning "or") to combine three boolean filters that check if the value in the education column is equal to each of those strings. The where function is used to keep only the rows in the education column that satisfy the filter3a condition, and the dropna function is used to remove any rows with missing values (represented by NaN). Finally, the count function is used to count the number of rows in the resulting filtered and cleaned data.

    For lower_education, the condition is the opposite of filter3a, i.e. that the value in the education column is not "Bachelors", "Masters", or "Doctorate". This condition is represented by the filter3b variable, which is created by using the logical ~ operator (meaning "not") to negate the filter3a variable, and the logical & operator (meaning "and") to combine three boolean filters that check if the value in the education column is not equal to each of those strings. The rest of the process is the same as for higher_education.
    """

    higher_education = df['education'].where(filter3a).dropna().count()
    lower_education = df['education'].where(filter3b).dropna().count() 
    
    """
    This code is calculating the percentage of people in the dataset who have a salary of ">50K" and have either a Bachelors, Masters, or Doctorate degree (higher_education_rich) or do not have one of those degrees (lower_education_rich).

    The filter3 variable is a boolean filter indicating whether the salary is ">50K" or not. The filter3a variable is a boolean filter indicating whether the education level is a Bachelors, Masters, or Doctorate. The filter3b variable is the negation of filter3a, meaning it indicates whether the education level is not a Bachelors, Masters, or Doctorate.

    The df['education'].where(filter3 & filter3a).dropna().count() expression gets the education column and filters it using the filter3 and filter3a filters, which returns a new Series with only the rows that meet both conditions. The .dropna() method removes any rows with missing values (NaN) and the .count() method counts the number of remaining rows. This value is then divided by the higher_education variable, which is the total number of people with a Bachelors, Masters, or Doctorate degree, and then multiplied by 100 and rounded to 1 decimal point to get the percentage. The same process is done for the lower_education_rich variable, but using the filter3b filter instead of the filter3a filter.
    """

    # percentage with salary >50K
    higher_education_rich = round(df['education'].where(filter3 & filter3a).dropna().count() / higher_education * 100,1)
    lower_education_rich = round(df['education'].where(filter3 & filter3b).dropna().count() / lower_education * 100,1)
    
    """
    The code retrieves the minimum number of hours per week worked by any individual in the dataset. It does this by calling the min() method on the hours-per-week column of the dataframe df. The min() method returns the minimum value in the column, which in this case is the minimum number of hours per week worked.
    """


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    """
    The code above is creating a new dataframe called min_work_h_salary by selecting rows from the dataframe df that meet two conditions:

    The value in the column 'hours-per-week' is equal to the minimum value of this column in the dataframe df.
    The value in the column 'salary' is equal to '>50K'.
    The resulting dataframe min_work_h_salary will contain all rows from df that meet both these conditions.
    """

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    min_work_h_salary = df[(df['hours-per-week'] == min_work_hours) & filter3]
    
    """
    This code is calculating the number of people in the dataset who work the minimum number of hours per week and have a salary of over 50k (haves) and the number of people who work the minimum number of hours per week in general (have_nots). The min_work_h_salary dataframe is created by filtering the original dataframe df to only include rows where the number of hours worked per week is equal to the minimum number of hours worked per week in the dataset and the salary is over 50k. The haves variable is then calculated by taking the length of the index of the min_work_h_salary dataframe, and the have_nots variable is calculated by taking the length of the index of a dataframe created by filtering the original dataframe to only include rows where the number of hours worked per week is equal to the minimum number of hours worked per week in the dataset.
    """

    haves = len(min_work_h_salary.index)
    have_nots = len(df[(df['hours-per-week'] == min_work_hours)].index)
    
    """
    This code calculates the percentage of people who earn more than $50,000 per year among the group of people who work the minimum number of hours per week. It does this by first finding the number of people in this group who earn more than $50,000 per year (haves). It then finds the total number of people in this group (have_nots). Finally, it divides haves by have_nots and multiplies the result by 100 to express it as a percentage.
    """

    rich_percentage = haves / have_nots * 100
    
    """
    This code creates a new dataframe country_list with a single column called "native-country" containing all the unique values from the "native-country" column in the original dataframe df. Two new columns, "High_Earners" and "High_Earners_Ratio", are then added to this dataframe, both initialized to 0. "High_Earners" will later be used to store the number of high earners (people with salary ">50K") in each country, and "High_Earners_Ratio" will be used to store the ratio of high earners to total number of people in each country.
    """

    # What country has the highest percentage of people that earn >50K?
    country_list = pd.DataFrame(data=df['native-country'].unique(), columns = ["native-country"])
    country_list['High_Earners'] = 0
    country_list['High_Earners_Ratio'] = 0
    
    """
    This code is setting the index of the country_list dataframe to the 'native-country' column. The index is used to identify each row in a dataframe and is usually a series of integers starting from 0. However, it is possible to set the index to be a column in the dataframe, which can be useful for organizing and accessing data. In this case, the 'native-country' column will be used as the index for the rows in the country_list dataframe.
    """

    country_list.set_index('native-country')
    
    """
    The code initializes a filter filter3 that is used to filter rows of the df dataframe based on the value of the salary column. Specifically, the filter will select only rows where the value of the salary column is ">50K". This filter can be used to select a subset of rows from the dataframe by applying it to the dataframe using the df.where() method.
    """

    filter3 = df['salary'] == '>50K' 
    
    """
    This code is iterating through the country_list DataFrame and using a combination of the iloc method and boolean indexing to update the values in the 'High_Earners' and 'High_Earners_Ratio' columns.

    The iloc method is used to select specific rows and columns from a DataFrame by their integer index. It takes two arguments: the row index and the column index. For example, df.iloc[0, 0] would select the value at the first row and first column of the DataFrame df.

    The for loop iterates through each row of country_list. The i variable is the index of the row, and row is a Series object representing the row. The iloc method is used to update the value of the 'High_Earners' column by selecting the current row and the 1st column (index 1) of country_list. The where method is used to select only the rows in the original DataFrame df that meet the conditions specified by the filter3 and filter6 filters, which are combined using the & operator. The dropna method is used to remove any rows with missing values. Finally, the count method is used to count the number of rows in the resulting filtered DataFrame.

    The 'High_Earners_Ratio' column is updated in a similar way, but the result is divided by the count of rows in the original DataFrame df that meet the filter6 condition, and then multiplied by 100 to express the result as a percentage.
    """

    for i, row in country_list.iterrows():
        filter6 = df['native-country'] == row['native-country']
        country_list.iloc[i, 1] = df['native-country'].where(filter3 & filter6).dropna().count()
        country_list.iloc[i, 2] = country_list.iloc[i, 1] / df['native-country'].where(filter6).dropna().count() * 100

        """
        This code is selecting the rows in the country_list dataframe that have the maximum value in the columns 'High_Earners' or 'High_Earners_Ratio', respectively. The .idxmax() method returns the index of the row with the maximum value in the given column. The .loc[] method is then used to select the row at that index.
        """
    country_list.loc[country_list['High_Earners'].idxmax()]
    country_list.loc[country_list['High_Earners_Ratio'].idxmax()]

    """
    This code is selecting the row in the country_list dataframe that has the highest value in the 'High_Earners_Ratio' column using the idxmax() function and assigning the value in the 'native-country' column of that row to the variable highest_earning_country. It is also assigning the value in the 'High_Earners_Ratio' column of that row to the variable highest_earning_country_percentage, after rounding it to one decimal place using the round() function.
    """
    highest_earning_country = country_list.loc[country_list['High_Earners_Ratio'].idxmax(), 'native-country']
    highest_earning_country_percentage = round(country_list.loc[country_list['High_Earners_Ratio'].idxmax(), 'High_Earners_Ratio'],1)

    """
    This code is creating a new dataframe called df_filtered that is filtered to only include rows from the original dataframe df where the value in the native-country column is 'India' and the value in the salary column is '>50K'. It then calculates the value count for each unique occupation in this filtered dataframe and returns the occupation with the highest value count using the idxmax() method. This value is stored in the variable top_IN_occupation.
    """
    # Identify the most popular occupation for those who earn >50K in India.
    df_filtered = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = df_filtered['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    """
    This code is part of a function that calculates and prints out a set of statistics based on a dataset contained in a CSV file. The function reads in the CSV file using the pandas library and stores it in a DataFrame called df. The function then calculates various statistics based on the data in the DataFrame, such as the average age of men, the percentage of people with Bachelors degrees, and the percentage of people with higher education who earn more than 50K. It also calculates the country with the highest percentage of rich people and the top occupations in India. Finally, the function has an optional argument called print_data which, if set to True, will print out all of the calculated statistics.
    """
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

        """
        This code defines a function calculate_demographic_data which processes a CSV file containing demographic data and calculates various statistics about the data. It then returns a dictionary containing these statistics. The function has a parameter print_data which, if set to True, will print the calculated statistics to the console. The function starts by reading in the CSV file using the read_csv function from the pandas library and storing the resulting data in a DataFrame object called df. It then calculates various statistics about the data, such as the average age of men, the percentage of people with Bachelors degrees, and the country with the highest percentage of people earning over $50,000 per year. Finally, the function returns a dictionary containing these statistics.
        """
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
