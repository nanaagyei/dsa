"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. 
If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        left = 0
        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        result, resultLen = [-1, -1], float("infinity")
        have = 0
        need = len(countT)

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
        left, right = result

        return s[left: right + 1] if resultLen != float("infinity") else ""  # return the substring from left to right + 1.  # return the substring from left