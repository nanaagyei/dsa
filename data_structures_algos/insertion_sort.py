
def insertion_sort(arr): 
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(j, j-1, arr)
            j -= 1
    
    return arr


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]