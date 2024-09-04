"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

- LRUCache(int capacity) Initialize the LRU cache of size capacity.
- int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.cache = {}

        # initialize dummy nodes on the left for the least recently used 
        # and dummy nodes on the right for the most recently used
        self.left, self.right = Node(0, 0), Node(0, 0) 

        # start the cache by connect the left and right nodes since the cache will start empty
        self.left.next = self.right 
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]