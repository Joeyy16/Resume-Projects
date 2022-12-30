

"""
This is a function definition in Python called arithmetic_arranger. It takes two parameters:

1. problems: a list of strings representing arithmetic problems, such as "1 + 2" or "5 - 3"

2. val (optional): a boolean value indicating whether the function should return the results of 
the arithmetic problems in addition to arranging them. The default value for val is False.

The function begins by defining an empty string called arranged_problems. If the length of the 
list problems is greater than 5, the function sets arranged_problems to the string "Error: Too many 
problems." and then returns arranged_problems. This means that if the function is called with more than 
5 problems in the list, it will immediately return the string "Error: Too many problems." without doing 
any further processing.
"""
def arithmetic_arranger(problems, val=False): 
  arranged_problems = ''
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems

    """
    This code is defining a list called operations that consists of the operators in the arithmetic problems. 
    The operations list is created using a list comprehension and the map() function.

    Here's how it works:

    The map() function applies the lambda function (an anonymous function) to each element in the problems list. 
    The lambda function takes a single argument x, which is a string representing an arithmetic problem.
    The lambda function splits the string x into a list of strings using the split() method, and returns the second element 
    of the list (which is the operator). For example, if x is the string "1 + 2", the lambda function would return "+".

    The map() function returns a map object that can be converted into a list using the list() function.
    Once the operations list has been created, the code checks to see if it consists solely of the "+" operator or the "-" operator,
    or if it contains both "+" and "-". If the operations list does not meet either of these criteria, the function sets arranged_problems 
    to the string "Error: Operator must be '+' or '-'." and returns arranged_problems. 
    This means that if any of the arithmetic problems use an operator other than "+" or "-", or if the list of problems contains both "+" and "-", 
    the function will immediately return the string "Error: Operator must be '+' or '-'." without doing any further processing.
    """

  # list of all operations in str format
  operations = list(map(lambda x: x.split()[1], problems))
  if set(operations) != {'+', '-'} and len(set(operations)) != 2:
    arranged_problems = "Error: Operator must be '+' or '-'."
    return arranged_problems

    """
    This code is creating a list called numbers that consists of the operands (numbers) in the arithmetic problems. It does this by 
    iterating through each arithmetic problem in the list problems, and using the split() method to split each problem into a list of strings.

    Here's how it works:

    The code defines an empty list called numbers.
    It uses a for loop to iterate through each arithmetic problem in the list problems. For each iteration, it assigns the current problem to the variable i.
    The code splits i into a list of strings using the split() method. For example, if i is the string "1 + 2", the split() method will return the list 
    ["1", "+", "2"]. This list is assigned to the variable p.
    The code uses the extend() method to add the first and third elements of p (which are the operands) to the numbers list.
    The for loop continues until all of the arithmetic problems have been processed, at which point the numbers list will contain all of the operands in the problems.
    At the end of this code, numbers will be a list of strings containing all of the operands in the arithmetic problems. For example, if problems is 
    ["1 + 2", "3 - 4", "5 - 6"], numbers will be ["1", "2", "3", "4", "5", "6"].
    """

  numbers = []  # list of all operands in str format
  for i in problems:
    p = i.split()
    numbers.extend([p[0], p[2]])

    """
    This code is checking to see if all of the elements in the numbers list are digits. It does this using a combination of the all() function and the map() function.

    Here's how it works:

    The map() function applies the lambda function (an anonymous function) to each element in the numbers list. The lambda function takes a single argument x, which is a string representing a number.
    The lambda function uses the isdigit() method to check if x consists solely of digits. If x consists solely of digits, isdigit() returns True. Otherwise, it returns False.
    The map() function returns a map object that can be passed to the all() function. The all() function returns True if all elements in the map object are True, and False otherwise.
    If the all() function returns False, it means that at least one element in the numbers list is not a digit. In this case, the code sets arranged_problems to the string "Error: Numbers must only contain digits." and returns arranged_problems. This means that if any of the operands in the arithmetic problems contain a non-digit character, the function will immediately return the string "Error: Numbers must only contain digits." without doing any further processing.
    """

  if not all(map(lambda x: x.isdigit(), numbers)):
    arranged_problems = "Error: Numbers must only contain digits."
    return arranged_problems

    """
    This code is checking to see if all of the elements in the numbers list are four digits or fewer. It does this using a combination of the all() function and the map() function.

    Here's how it works:

    The map() function applies the lambda function (an anonymous function) to each element in the numbers list. The lambda function takes a single argument x, which is a string representing a number.
    The lambda function uses the len() function to get the length of x. If the length of x is less than 5, the lambda function returns True. Otherwise, it returns False.
    The map() function returns a map object that can be passed to the all() function. The all() function returns True if all elements in the map object are True, and False otherwise.
    If the all() function returns False, it means that at least one element in the numbers list has more than four digits. In this case, the code sets arranged_problems to the string "Error: Numbers cannot be more than four digits." and returns arranged_problems. This means that if any of the operands in the arithmetic problems have more than four digits, the function will immediately return the string "Error: Numbers cannot be more than four digits." without doing any further processing.
    """

  if not all(map(lambda x: len(x) < 5, numbers)):
    arranged_problems = "Error: Numbers cannot be more than four digits."
    return arranged_problems

    """
    This code is creating three strings: top_row, dashes, and solutions. These strings are used to format the arithmetic problems in a visually appealing way.

    Here's how it works:

    The code defines three empty strings: top_row, dashes, and solutions.
    It creates a list called values that consists of the results of the arithmetic problems. The values list is created using a list comprehension and the map() function. The map() function applies the lambda function (an anonymous function) to each element in the problems list. The lambda function takes a single argument x, which is a string representing an arithmetic problem. The lambda function uses the eval() function to evaluate the arithmetic problem and return the result.
    The code uses a for loop to iterate through the numbers list in pairs of two. For each iteration, it assigns the index to the variable i.
    The code calculates the width of the space needed for the operands in the current pair using the max() function and the len() function. The max() function returns the maximum of the lengths of the two operands. The len() function returns the length of a string. The width of the space is calculated by adding 2 to the maximum length.
    The code uses the rjust() method to right-justify the operands in the current pair within the space calculated in the previous step. The rjust() method takes two arguments: the string to be right-justified and the width of the space to right-justify it in. It returns a new string that is right-justified within the specified space. The right-justified operands are then added to the top_row and solutions strings.
    The code uses the * operator to create a string of dashes that is the same length as the space calculated in step 4. This string of dashes is then added to the dashes string.
    If the current index i is not the second-to-last index in the numbers list, the code adds four spaces to the top_row, dashes, and solutions strings. This is done to add spacing between the pairs of operands in the final output.
    At the end of this code, top_row will contain the operands in the arithmetic problems, right-justified and spaced apart, dashes will contain a row of dashes that is the same width as top_row, and solutions will contain the results of the arithmetic problems, right-justified and spaced apart. These three strings can be used to create a visually appealing arrangement of the arithmetic problems.
    """

  top_row = ''
  dashes = ''
  values = list(map(lambda x: eval(x), problems))
  solutions = ''
  for i in range(0, len(numbers), 2):
    space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
    top_row += numbers[i].rjust(space_width)
    dashes += '-' * space_width
    solutions += str(values[i // 2]).rjust(space_width)
    if i != len(numbers) - 2:
      top_row += ' ' * 4
      dashes += ' ' * 4
      solutions += ' ' * 4
      
    """
    This code is creating a string called bottom_row that consists of the operators in the arithmetic problems and the second operand in each pair of operands.

    Here's how it works:

    The code defines an empty string called bottom_row.
    It uses a for loop to iterate through the numbers list in pairs of two, starting with the second operand in each pair. For each iteration, it assigns the index to the variable i.
    The code calculates the width of the space needed for the second operand in the current pair using the max() function and the len() function. The max() function returns the maximum of the lengths of the two operands. The len() function returns the length of a string. The width of the space is calculated by adding 1 to the maximum length.
    The code uses the rjust() method to right-justify the second operand in the current pair within the space calculated in the previous step. The rjust() method takes two arguments: the string to be right-justified and the width of the space to right-justify it in. It returns a new string that is right-justified within the specified space.
    The code adds the operator for the current pair (which is stored in the operations list) to the beginning of the bottom_row string.
    If the current index i is not the last index in the numbers list, the code adds four spaces to the bottom_row string. This is done to add spacing between the pairs of operands in the final output.
    At the end of this code, bottom_row will contain the operators and second operands in the arithmetic problems, spaced apart. This string can be used to create a visually appealing arrangement of the arithmetic problems.
    """

  bottom_row = ''
  for i in range(1, len(numbers), 2):
    space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
    bottom_row += operations[i // 2]
    bottom_row += numbers[i].rjust(space_width)
    if i != len(numbers) - 1:
      bottom_row += ' ' * 4

    """
    This code is creating the final string to be returned by the arithmetic_arranger() function. It does this by joining the top_row, bottom_row, and dashes strings with newline characters.

    Here's how it works:

    If the value of the val parameter is True, the code uses the join() method to join the top_row, bottom_row, dashes, and solutions strings with newline characters. The resulting string is assigned to arranged_problems.
    If the value of the val parameter is False, the code uses the join() method to join the top_row, bottom_row, and dashes strings with newline characters. The resulting string is assigned to arranged_problems.
    The function returns arranged_problems.
    If the val parameter is True, the arranged_problems string will contain the operands, operators, and results of the arithmetic problems, with each line separated by a newline character. If the val parameter is False, the arranged_problems string will contain the operands and operators of the arithmetic problems, with each line separated by a newline character.
    """

  if val:
    arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
  else:
    arranged_problems = '\n'.join((top_row, bottom_row, dashes))
  return arranged_problems
