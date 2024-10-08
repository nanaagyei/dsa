"""
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40
Explanation: The optimal path is 15 -> 20 -> 5 with a path sum of 15 + 20 + 5 = 40.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            res = max(res, left + right + root.val)

            return max(left, right) + root.val
        dfs(root)
        return res
        