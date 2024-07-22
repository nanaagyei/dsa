
# Exercise 1
# Given an array of positive numbers, write a function that returns
# the greatest product of any three numbers

from quicksort import SortableArray
def greatest_prod(array):
    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array) - 1)
    return array[-1] * array[-2] * array[-3]


arr = [4, 9, 1, 2, 8, 6, 5, 7, 3, 0]
print(greatest_prod(arr))

# Exercise 2
def missing_number(array):
    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array) - 1)
    for i in range(len(array)):
        if array[i] == i:
            return i
    
    return None

# Exercise 3
# Write three different implementations of a function that finds the
# greatest number within an array

# O(N^2)
def greatest_number1(array):
    for i in range(len(array)):
        isGreatestNumber = True
        for j in range(len(array)):
            if array[j] > array[i]:
                isGreatestNumber = False
        
        if isGreatestNumber:
            return array[i]

# O(NlogN)
def greatest_number2(array):
    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array) - 1)
    return array[-1]


# O(N)
def greatest_number3(array):
    greatest = array[0]
    for i in range(len(array)):
        if array[i] > greatest:
            greatest = array[i]
    
    return greatest

