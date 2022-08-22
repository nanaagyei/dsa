# Question 1
# Use recursion to write a function that accepts an array of strings and returns
# the total number of characters across all the strings

def char_sum(array):
    if len(array) == 0:
        return 0
    return len(array[0]) + char_sum(array[1:len(array)])

# array = ["ab", "c", "def", "ghij"]
# print(char_sum(array))

########################################################################################
# Question 2
# Use recursion to write a function that accepts an array of numbers and
# returns a new array containing just the even numbers

def even_numbers(array):
    if len(array) == 0:
        return []
    
    if array[0] % 2 == 0:
        return [array[0]] + even_numbers(array[1:len(array)])
    else:
        return even_numbers(array[1:len(array)])

# array = [1, 2, 3, 4, 5]
# print(even_numbers(array))

########################################################################################
# Question 3
# The Triangular Numbers
# Write a function that accepts a number for N and returns the correct number
# from the series

def triangular_number(n):
    if n == 1:
        return 1
    return n + triangular_number(n - 1)

# print(triangular_number(7))

#######################################################################################
# Question 4
# Use recursion to write a function that accepts a string and returns the first
# index that contains the character "x".

def contains_x(string, index=0):
    if index >= len(string):
        return None
    if string[index] == "x":
        return index
    else:
        return contains_x(string, index + 1)

# text = "abcdefghijklmnopqrstuvwxyz"
# print(contains_x(text))

#####################################################################################
# Question 5
# The "Unique Paths" problem. Write a function that accepts a number of rows
# and a number of columns, and calculates the number of possible "shortest"
# from the upper-leftmost square of the grid to the lower-rightmost square

def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
