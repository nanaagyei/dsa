"""
You are given the head of a linked list of length n. 
Unlike a singly linked list, each node contains an additional pointer random, 
which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        oldtoCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldtoCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldtoCopy[cur]
            copy.next = oldtoCopy[cur.next]
            copy.random = oldtoCopy[cur.random]
            cur = cur.next
        return oldtoCopy[head]