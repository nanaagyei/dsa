"""
Given two integer arrays pushed and popped each with distinct values, 
return true if this could have been the result of a sequence of push 
and pop operations on an initially empty stack, or false otherwise.
"""

class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack