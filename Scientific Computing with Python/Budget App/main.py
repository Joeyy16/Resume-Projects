# Entrypoint file 

# Imports the budget module and the create_spend_chart() function from the budget module.
import budget
from budget import create_spend_chart


food = budget.Category("Food") # Creates an object of the Category class from the budget module with the name "Food" and assigns it to the food variable.
food.deposit(1000, "initial deposit") # Calls the deposit() method on the food object with the amount 1000 and the description "initial deposit".
food.withdraw(10.15, "groceries") # Calls the withdraw() method on the food object with the amount 10.15 and the description "groceries".
food.withdraw(15.89, "restaurant and more food for dessert") # Calls the withdraw() method on the food object with the amount 15.89 and the description "restaurant and more food for dessert".
print(food.get_balance()) # Prints the balance of the food object using the get_balance() method.
clothing = budget.Category("Clothing") # Creates an object of the Category class from the budget module with the name "Clothing" and assigns it to the clothing variable.
food.transfer(50, clothing) # Calls the transfer() method on the food object with the amount 50 and the clothing object as arguments.
clothing.withdraw(25.55) # Calls the withdraw() method on the clothing object with the amount 25.55.
clothing.withdraw(100) # Calls the withdraw() method on the clothing object with the amount 100.
auto = budget.Category("Auto") # Creates an object of the Category class from the budget module with the name "Auto" and assigns it to the auto variable.
auto.deposit(1000, "initial deposit") # Calls the deposit() method on the auto object with the amount 1000 and the description "initial deposit".
auto.withdraw(15) # Calls the withdraw() method on the auto object with the amount 15.

# Prints the food, clothing, and auto objects using the __str__() method defined in the Category class.
print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto])) # Calls the create_spend_chart function

