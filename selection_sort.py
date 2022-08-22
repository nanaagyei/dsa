
def selection_sort(arr):
    for i in range(len(arr)): # Loop through the array
        min_index = i # Assign the index of the first element to the index of the current element
        for j in range(i+1, len(arr)): # Loop through the array from the current element to the last element
            if arr[j] < arr[min_index]: # If the element is less than the current minimum element
                min_index = j   # Assign the index of the element to the minimum index
        arr[i], arr[min_index] = arr[min_index], arr[i] # Swap the elements
    return arr