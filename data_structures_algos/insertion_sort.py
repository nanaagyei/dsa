
def insertion_sort(arr): 
    for i in range(1, len(arr)):
        key = arr[i] # Assign the value of the current element to key
        j = i - 1 # Assign the index of the previous element to j
        while j >= 0 and key < arr[j]: # Loop through the array from the last element to the first element
            arr[j + 1] = arr[j] # Shift the elements to the right
            j -= 1 # Decrease the index of the previous element by 1
        arr[j + 1] = key # Insert the key into the array
    return arr
