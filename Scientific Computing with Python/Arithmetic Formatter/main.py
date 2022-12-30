# This entrypoint file to be used in development. Start by reading README.md

"""
from pytest import main is an import statement in Python that imports the main() function from the pytest module.

The pytest module is a popular testing framework for Python that allows you to write test cases for your code and run them automatically. The main() function is the main entry point for running pytest from the command line. It takes a list of arguments and runs the test cases specified by those arguments.

For example, you could use the following command to run all test cases in the current directory:
"""


"""
from arithmetic_arranger import arithmetic_arranger is an import statement in Python that imports the arithmetic_arranger() function from the arithmetic_arranger module.
"""

from arithmetic_arranger import arithmetic_arranger

#Calling Function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])) #Prints called function


