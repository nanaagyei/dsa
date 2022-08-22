from random import randint

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

# if __name__ == "__main__":
#     array = [randint(1, 20) for i in range(10)]
#     print("Unsorted array: ", array)
#     print("Sorted array, ", bubble_sort(array))

