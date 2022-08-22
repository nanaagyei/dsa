
# Prints the sum of all the elements in the array
def array_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + array_sum(array[1:len(array)])

# array = [1, 2, 3, 4, 5]
# print(array_sum(array))

# Returns the number of x's in a string
def count_x(string):
    if not string:
        return 0
    if string[0] == "x":
        return 1 + count_x(string[1:len(string)])
    else:
        return count_x(string[1:len(string)])

# text = "axcsxxdxsxex"
# print(count_x(text))
