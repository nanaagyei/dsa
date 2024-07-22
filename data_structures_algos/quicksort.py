class SortableArray:
    def __init__(self, array):
        self.array = array
    
    def partition(self, left_pointer, right_pointer):
        # Choose the right-most element as the pivot.
        pivot_index = right_pointer

        pivot = self.array[pivot_index] # value of pivot index

        # start the right pointer immediately to the left of the pivot
        # i.e decrement by one
        right_pointer -= 1

        while True:

            # Move the left pointer to the right as long as it
            # points to a value that is less than the pivot
            while self.array[left_pointer] < pivot:
                left_pointer += 1
            
            # Move the right pointer to the left as long as it
            # points to a value that is greater than the pivot
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
            
            # Check whether the left pointer has reached or gone 
            # beyond the right pointer. if it has, break out of
            # the loop to begin swapping the pivot
            if left_pointer >= right_pointer:
                break
            else:
                # If the left pointer is still to the left of the right
                # pointer, we swap the values of the left and right pointers
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]

                # Then move the left pointer over to the right, gearing up 
                # for the next round of left and right pointer movements
                left_pointer += 1
        
        # Finally, we swap the value of the left pointer with the pivot
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]

        return left_pointer
    
    # Quicksort Algo
    def quicksort(self, left_index, right_index):
        # base case: the subarray has 0 or 1 elements
        if right_index - left_index <= 0:
            return
        
        # Partition the range of elements and grab the index of the pivot
        pivot_index = self.partition(left_index, right_index)

        self.quicksort(left_index, pivot_index - 1)

        self.quicksort(pivot_index + 1, right_index)

    # Quickselect Algo
    def quickselect(self, kth_lowest_value, left_index, right_index):
        # Base case (i.e if we reach an array containing only one value)
        if right_index - left_index <= 0:
            return self.array[left_index]
        
        # Partition the array and grab the index of the pivot
        pivot_index = self.partition(left_index, right_index)

        if kth_lowest_value < pivot_index:
            self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
        
        elif kth_lowest_value > pivot_index:
            self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        else:
            return self.array[pivot_index]

# Example
# arr = [0, 50, 20, 10, 60, 30]
# arr = [4, 9, 1, 2, 8, 6, 5, 7, 3, 0]
# sortarr = SortableArray(arr)
# sortarr.quicksort(0, len(arr) - 1)
# print(arr)
# sortable_array = SortableArray(arr)
# print(sortable_array.quickselect(5, 0, len(arr) - 1))
