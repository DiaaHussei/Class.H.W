###Lambda### 
'''
is a keyword in Python used to define anonymous functions.
 These functions are also known as lambda functions or lambda expressions.
  They are small, single-use functions that do not have a name and can be defined in-line. 
  Lambda functions are often used when we need to pass a simple function as an argument to another function.
  '''

#Example1:

'''
Suppose we have a list of numbers and we want to sort them in descending order.
 We can use the sorted() function with a lambda function as the key argument:'''

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sorted_numbers = sorted(numbers, key=lambda x: -x)

print(sorted_numbers)