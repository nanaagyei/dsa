import numpy as np
from random import randint
from matplotlib import pyplot as plt
from time import time

def bubble_sort(array):
    unsorted_until_index = len(array) - 1  # Assigned the index of the unsorted array to the last element
    sorted = False # Temporarily initialized sorted to True. Is changed to False when elements in the array are swapped or array is unsorted

    while not sorted: 
        sorted = True 
        # Loop through the array from the last element to the first element
        for i in range(unsorted_until_index):
            if array[i] > array[i+1]:
                sorted = False  # If the element is greater than the next element, the array is not sorted
                array[i], array[i+1] = array[i+1], array[i] # Swap the elements
        unsorted_until_index -= 1 # Decrease the index of the unsorted array by 1
    
    return array

if __name__ == "__main__":
    array = [randint(1, 20) for i in range(10)]
    print("Unsorted array: ", array)
    print("Sorted array, ", bubble_sort(array))

    num_elements = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    time_elapse = []

    for num in num_elements:
        array = [randint(1, 20) for i in range(num)]
        t0 = time()
        print("Sorted array, ", bubble_sort(array))
        t1 = time()
        time_elapse.append(t1-t0)
    
    plt.plot(num_elements, time_elapse, 'o-', label="Bubble Sort")
    plt.legend()
    plt.xlabel("Number of Elements")
    plt.ylabel("Time Elapse")
    plt.title("Time Complexity for Bubble Sort Algo")
    plt.show()
