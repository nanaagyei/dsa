class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

    def delete_at_pos(self, pos):
        temp = self.head
        prev = None
        count = 1
        while temp:
            if count == pos:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
            count += 1

    def delete_at_pos_recursive(self, pos):
        self.delete_at_pos_recursive_helper(self.head, pos, 0)

    def delete_at_pos_recursive_helper(self, temp, pos, count):
        if temp is None:
            return
        if count == pos:
            temp.next = temp.next.next
            return
        self.delete_at_pos_recursive_helper(temp.next, pos, count + 1)
    
    def countNodes(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev