class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
    
    def remove_head(self):
        removed_node = self.head
        self.head = self.head.next
        return removed_node


# implementing a queue with a doubly linked list
class Queue:
    def __init__(self):
        self.data = DoublyLinkedList()
    
    def enqueue(self, value):
        self.data.insert_at_end(value)
    
    def dequeue(self, value):
        removed_node = self.data.remove_head
        return removed_node
    
    def read(self):
        if not self.data.head:
            return None
        return self.data.head.data