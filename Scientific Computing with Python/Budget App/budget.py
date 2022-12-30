"""
This code defines a class named Category with a single method, the __init__() method. This method is the constructor method for the class, which is called when an object of the class is created.

The __init__() method has three instance variables:

description: This variable stores the description of the category. It is passed as an argument to the __init__() method and is assigned to the description instance variable.

ledger: This variable is a list that stores all the transactions made for the category. It is initialized as an empty list.

__balance: This variable stores the current balance of the category. It is initialized as 0.0. The double underscore before the variable name indicates that it is a "private" instance variable and should not be accessed directly from outside the class.

Note that the __init__() method has no return statement, it simply initializes the instance variables of the object.
"""

class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.__balance = 0.0
        
        """
        This code defines the __repr__() method for the Category class. The __repr__() method is a special method in Python that is called when the object needs to be represented as a string, for example when it is printed.

        The __repr__() method has the following logic:

        It initializes a variable header with the description of the category, centered within a line of 30 asterisks (*).
        It initializes a variable ledger as an empty string.
        It iterates over the items in the ledger instance variable using a for loop.
        For each item, it formats the description and amount values and assigns them to variables line_description and line_amount respectively.
        It then truncates the line_description and line_amount variables to 23 and 7 characters respectively.
        It appends the truncated line_description and line_amount variables to the ledger variable, separated by a space.
        It initializes a variable total with the current balance of the category, formatted as a string with 2 decimal places.
        It returns the concatenation of the header, ledger, and total variables.
        The __repr__() method returns a string representation of the Category object, which includes the description of the category, a list of the transactions in the ledger, and the current balance of the category.
        """

    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate ledger description and amount to 23 and 7 characters respectively
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.__balance)
        return header + ledger + total
    
    """
    This code defines the deposit() method for the Category class. The deposit() method is used to add money to the category's balance.

    The deposit() method has the following logic:

    It appends a dictionary to the ledger instance variable with the amount and description passed as arguments to the method.
    It increases the value of the __balance instance variable by the amount passed as an argument to the method.
    The deposit() method does not return anything, it simply updates the ledger and __balance instance variables of the Category object.
    """

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.__balance += amount
        
    """
    This code defines the withdraw() method for the Category class. The withdraw() method is used to subtract money from the category's balance.

    The withdraw() method has the following logic:

    It checks if the current balance minus the amount passed as an argument to the method is greater than or equal to zero.
    If the balance is sufficient, it appends a dictionary to the ledger instance variable with the amount passed as an argument to the method, negated and with the description passed as an argument to the method. It then decreases the value of the __balance instance variable by the amount passed as an argument to the method.
    If the balance is not sufficient, it does not update the ledger or __balance instance variables, and instead returns False.
    The withdraw() method returns True if the withdrawal was successful, or False if the balance was insufficient.
    """

    def withdraw(self, amount, description=""):
        if self.__balance - amount >= 0:
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.__balance -= amount
            return True
        else:
            return False
        
    """
    This code defines the get_balance() method for the Category class. The get_balance() method is used to get the current balance of the category.

    The get_balance() method has the following logic:

    It returns the value of the __balance instance variable of the Category object.
    The get_balance() method returns the current balance of the category as a float.
    """

    def get_balance(self):
        return self.__balance
    
    """
    This code defines the transfer() method for the Category class. The transfer() method is used to transfer money from the current category to another category.

    The transfer() method has the following logic:

    It calls the withdraw() method of the current Category object, passing the amount argument and a description of the transfer. If the withdraw() method returns True, it indicates that the balance is sufficient and the transfer can proceed.
    If the withdraw() method returns True, it calls the deposit() method of the category_instance argument passed to the transfer() method, passing the amount argument and a description of the transfer.
    If the withdraw() method returns False, it does not call the deposit() method of the category_instance and instead returns False.
    The transfer() method returns True if the transfer was successful, or False if the balance was insufficient.
    """

    def transfer(self, amount, category_instance):
        if self.withdraw(amount, "Transfer to {}".format(category_instance.description)):
            category_instance.deposit(amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False
    
    """
    This code defines the check_funds() method for the Category class. The check_funds() method is used to check if the balance of the category is sufficient to cover a certain amount of money.

    The check_funds() method has the following logic:

    It compares the value of the __balance instance variable of the Category object to the amount argument passed to the check_funds() method.
    If the __balance is greater than or equal to the amount, it returns True. Otherwise, it returns False.
    The check_funds() method returns a boolean value indicating whether the balance of the category is sufficient to cover the specified amount.
    """

    def check_funds(self, amount):
        if self.__balance >= amount:
            return True
        else:
            return False


"""
This code defines the create_spend_chart() function, which is used to create a chart that displays the total amount spent in each of the specified categories.

The create_spend_chart() function has the following logic:

It initializes an empty list called spent_amounts, which will be used to store the total amount spent in each category.
It iterates over the list of categories passed to the function.
For each category in the list, it initializes a variable called spent to 0 and iterates over the ledger of the category.
For each item in the ledger, it checks if the amount of the item is less than 0. If it is, it adds the absolute value of the amount to the spent variable. This is done because we only want to count the amount spent in the category (which will be represented by negative values in the ledger), not the amount deposited (which will be represented by positive values).
After the inner loop finishes iterating over all the items in the ledger, it appends the value of spent to the spent_amounts list, rounded to two decimal places.
The function returns the spent_amounts list, which contains the total amount spent in each category.
"""
def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))
        
    """
    This code calculates the percentage spent in each category and rounds the result down to the nearest multiple of 10.

    The total variable is calculated by summing up all the amounts spent in each category and rounding the result to 2 decimal places.

    The spent_percentage list is then calculated using a lambda function and the map function. The lambda function takes in an amount and divides it by the total to get the percentage spent in that category. This result is then multiplied by 10 to get the percentage in tens. The floor division // operator is then used to round the result down to the nearest integer. Finally, the result is multiplied by 10 again to get the percentage in multiples of 10.

    For example, if amount is 50 and total is 100, the percentage spent in that category would be 50. Multiplying this by 10 gives 500, which when floor divided by 1 gives 500. Multiplying this result by 10 again gives 5000, which is the percentage spent in that category rounded down to the nearest multiple of 10.
    """

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    """
    The header variable is a string that contains the text "Percentage spent by category" followed by a new line character. This string will be used as a header in the output of the create_spend_chart() function. The header is intended to provide context for the data that follows it in the output.
    """
    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    """
    This code is constructing a visual representation of the percentage of money spent in each category, in the form of a bar chart.

    The chart variable is initialized as an empty string, which will be used to store the chart as it is built. Then, a loop is started that iterates over values from 0 to 100 in steps of 10 (range(0, 101, 10)). For each iteration of the loop, a line of the chart is constructed.

    First, the current value of the loop variable is added to the chart string, right-aligned to take up 3 characters (str(value).rjust(3)). Then, a vertical bar character is added to the chart string (+ '|').

    Next, another loop iterates over the spent_percentage list. For each element in the list, the code checks if the percentage is greater than or equal to the current value of the outer loop variable. If it is, an "o" character is added to the chart string. If not, two spaces are added to the chart string.

    After the inner loop has completed, a newline character is added to the chart string (+ " \n") and the outer loop continues with the next value.

    When the outer loop has completed, the chart string will contain the full chart, with each line representing 10% of the total spent and the "o" characters indicating the amount spent in each category. The chart is then returned as output.
    """
    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    """
    This code is creating the footer of the spend chart which will be displayed at the bottom of the chart. The footer consists of a series of dashes that are as wide as the chart, followed by the descriptions of the categories.

    The footer starts with a string of four spaces followed by a series of dashes that are as wide as the chart. The width of the chart is calculated by taking the number of categories and multiplying it by three (since each category takes up three characters in the chart). Then, a newline character is added to the end of the string.

    Next, a list of the descriptions of the categories is created using a list comprehension. The list comprehension maps the description attribute of each category to a new list. The resulting list is stored in the descriptions variable.

    The maximum length of the descriptions in the list is then determined using the max function and the len function. The max function returns the largest value in an iterable, and the len function returns the length of a string.

    A new list of the descriptions is then created using a list comprehension. This list comprehension maps the ljust method of each description to a new list. The ljust method left-justifies a string by padding it with spaces until it reaches the desired length. The desired length is the maximum length of the descriptions that was previously calculated. This new list is stored in the descriptions variable.

    Finally, the zip function and the * operator are used to iterate over the elements of descriptions as separate arguments. The * operator is used to unpack the elements of descriptions so that they can be passed as separate arguments to the zip function. The zip function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the iterables.

    The resulting iterator is then iterated over using a for loop. On
    """
    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    """
    The code you provided is creating a chart that shows the percentage of money spent in each category.

    The first step is to calculate the percentage of money spent in each category by dividing the amount spent in the category by the total amount spent in all categories and multiplying the result by 100. The resulting percentages are rounded down to the nearest 10, as we are only interested in the tens place. The list of rounded percentages is stored in the spent_percentage variable.

    Next, the chart is generated by iterating over a range of values from 0 to 100 in steps of 10, with the highest value being at the top of the chart and the lowest value at the bottom. For each iteration, a row is added to the chart with the current value at the beginning, followed by a "o" for each category where the percentage of money spent is greater than or equal to the current value, and spaces for each category where the percentage is less than the current value. The resulting chart is stored in the chart variable.

    The footer of the chart is created by concatenating the descriptions of the categories, aligning them to the left and padding them with spaces so that they have the same length. The footer is then added to the chart by iterating over the list of descriptions and adding each character in the descriptions to the footer, centered in a column of 3 spaces.

    Finally, the header, chart, and footer are combined and returned as the result, with the trailing newline character stripped.
    """
    return (header + chart + footer).rstrip("\n")
