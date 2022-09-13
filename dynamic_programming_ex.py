# EXercise 1
# The following function accepts an array of numbers ad returns the sum, as long as
# a particular number doesn't bring the sum above 100. If a particular number makes 
# the sum higher than 100, that number is ignored. However this function makes unnecessary
# recursive calls. Fix the code to eliminate the unnecessary function

# Function(unmodified version)
def add_until_100(array):
    if len(array) == 0:
        return 0
    if array[0] + add_until_100(array[1, len(array)]) > 100:
        return add_until_100(array[1, len(array)])
    else:
        return array[0] + add_until_100(array[1, len(array)])

# Modified version
def add_to_100(array):
    if len(array) == 0:
        return 0
    sum_to_100 = add_until_100(array[1, len(array)])
    if array[0] + sum_to_100 > 100:
        return sum_to_100
    else:
        return array[0] + sum_to_100

##############################################################################################################

# Exercise 2
# Use memoization to modify the function

def golomb(n):
    if n == 1:
        return 1
    return 1 + golomb(n - golomb(golomb(n-1)))

# Modified version
def new_golomb(n, memo):
    if n == 1:
        return 1
    memo = {}
    
    if not memo.get(n):

        memo[n] = 1 + new_golomb(n - new_golomb(new_golomb(n-1, memo), memo), memo)
    
    return memo[n]

##############################################################################################################

# Exercise 3
# Use memoization to improve its efficiency of the solution to "Unique Paths"

def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

# Modified version
def unique_paths_mod(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1
    
    if not memo.get([rows, columns]):

        memo[[rows, columns]] = unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
    
    return memo[[rows, columns]]