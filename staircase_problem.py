
# Finds the number of possible paths to take to reach the top of a staircase
# with n steps given one can only take one, two or three steps at a time

def number_of_paths(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)

# print(number_of_paths(6))
