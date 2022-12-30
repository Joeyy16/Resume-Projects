# This entrypoint file to be used in development. Start by reading README.md

"""
This code does the following:

Imports the budget module and the create_spend_chart() function from the budget module.
Creates an object of the Category class from the budget module with the name "Food" and assigns it to the food variable.
Calls the deposit() method on the food object with the amount 1000 and the description "initial deposit".
Calls the withdraw() method on the food object with the amount 10.15 and the description "groceries".
Calls the withdraw() method on the food object with the amount 15.89 and the description "restaurant and more food for dessert".
Prints the balance of the food object using the get_balance() method.
Creates an object of the Category class from the budget module with the name "Clothing" and assigns it to the clothing variable.
Calls the transfer() method on the food object with the amount 50 and the clothing object as arguments.
Calls the withdraw() method on the clothing object with the amount 25.55.
Calls the withdraw() method on the clothing object with the amount 100.
Creates an object of the Category class from the budget module with the name "Auto" and assigns it to the auto variable.
Calls the deposit() method on the auto object with the amount 1000 and the description "initial deposit".
Calls the withdraw() method on the auto object with the amount 15.
Prints the food, clothing, and auto objects using the __str__() method defined in the Category class.
Calls the `create_spend_
"""

import budget
from budget import create_spend_chart


food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

