"""
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the number of nodes in the tree

#-----------------------------------------------------------------------------------------------#

# BFS
    def maxDepth2(self, root: TreeNode) -> int:
        level = 0

        if not root:
            return level

        queue = deque([root])

        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return level

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the number of nodes in the tree

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print(Solution().maxDepth(root))