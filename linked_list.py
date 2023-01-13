class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # for a doubly linked list
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)

# A singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # read value from a linked list at an index
    def read(self, index):
        current_node = self.head
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1
            if not current_node:
                return None
        return current_node.data
    
    # returns the index of a value in a linked list
    def index(self, value):
        current_node = self.head
        current_index = 0
        while current_node:
            if current_node.data == value:
                return current_index
            current_node = current_node.next
            current_index += 1
        return None
    
    # inserts data/value at the beginning of a linked list
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # inserts data/value at at given index of a linked list
    def insert_at_index(self, index, data):
        new_node = Node(data)
        current_node = self.head
        current_index = 0

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # loop through the linked list until the index is reached
        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1
            if not current_node:
                return None
        new_node.next = current_node.next
        current_node.next = new_node

    # prints elements in the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete(self, key):
        temp = self.head
        prev = None
        while temp:
            if temp.data == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next

    # deletes a node at given index
    def delete_at_index(self, index):
        current_node = self.head
        if index == 0:
            self.head = current_node.next
            return
        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        
        node_after_deleted = current_node.next.next
        current_node.next = node_after_deleted

    def delete_at_pos_recursive(self, pos):
        self.delete_at_pos_recursive_helper(self.head, pos, 0)

    def delete_at_pos_recursive_helper(self, temp, pos, count):
        if temp is None:
            return
        if count == pos:
            temp.next = temp.next.next
            return
        self.delete_at_pos_recursive_helper(temp.next, pos, count + 1)
    
    # returns the length of a linked list
    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
    # reversing a linked list
    # look at this moreeeee########
    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev


# A doubly linked list
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    # inserting value at the end of a doubly linked list
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
