"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        size_s1 = len(s1)
        size_s2 = len(s2)

        for right in range(size_s2):
            while (right - left + 1) <= size_s1:
                right += 1
            if self.isPermutation(s1, s2[left: right]):
                return True
            else:
                left += 1
        
        return False

    
    def isPermutation(self, str1, str2):
        if len(str1) != len(str2):
            return False
            
        count1 = {}
        count2 = {}

        for i in range(len(str1)):
            count1[str1[i]] = 1 + count1.get(str1[i], 0)
            count2[str2[i]] = 1 + count2.get(str2[i], 0)
        
        for char in count1:
            if count1[char] != count2.get(char, 0):
                return False
        
        return True