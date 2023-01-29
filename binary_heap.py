class Heap:
    # created an array-based heap data structure
    def __init__(self):
        self.data = []
    
    # returns the root node of the tree
    def root_node(self):
        return self.data[0]
    
    # returns the rightmost node at the bottom level of the tree
    def last_node(self):
        return self.data[-1]
    
    # returns the index of the left child of a parent node. 
    # it uses a formula since we are using an array
    def left_child_index(self, index):
        return (index * 2) + 1
    
    # returns the index of the right child of the parent node
    def right_child_index(self, index):
        return (index * 2) + 2
    
    # returns the index of the parent node
    def parent_node_index(self, index):
        return (index * 1) // 2
    
    # inserting a value into a max-heap data structure
    def insert(self, value):
        # we add the value to the end of the array (in this case, the rightmost node of at the bottom leve of the heap)
        self.data.append(value)

        # keep track of the index of the new node
        new_node_index = len(self.data) - 1

        # this loop follows the "trickling up algorithm"
        # while the node is not the root node or the parent node is less than the newly inserted node, we do the following
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_node_index(new_node_index)]:

            # swap the parent node with the new node
            self.data[self.parent_node_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_node_index(new_node_index)]

            # the new node becomes the parent node on that level (row) so we keep track of that index and repeat the process
            new_node_index = self.parent_node_index(new_node_index)

    # Delete the root node from the heap
    def delete(self):

        # deleting the root node basically means we replace the root node with the last node
        self.data[0] = self.data.pop()

        # keep track of the index of the root node (essentially the node we will trickle down the tree)
        trickle_node_index = 0

        # check if the node has a child node greater than it
        while self.has_greater_child(trickle_node_index):

            # find the index of that greater child node
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            
            # swap the parent node (in this case the trickle node) with the larger child node
            self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]

            # the new trickle node index becomes the index of the larger child node since they swapped positions
            trickle_node_index = larger_child_index
    
    def has_greater_child(self, index):
        # checks whether the node has a left or right child node that is greater than the node at index
        return (self.data[self.left_child_index(index)] and self.data[self.left_child_index(index)] > self.data[index]) or (self.data[self.right_child_index(index)] and self.data[self.right_child_index(index)] > self.data[index])
    
    # finds the index of the larger child node
    def calculate_larger_child_index(self, index):
        # if the parent node does not have a right child, it returns the index of the left child node
        # we do not do the same for the left child because the heap cannot have a right child node and an empty left child node
        # that would not make it complete
        if not self.data[self.right_child_index(index)]:
            return self.left_child_index(index)
        
        # if the parent node has both left and right, we check which one is greater and return the index of that greater child node
        if self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)
