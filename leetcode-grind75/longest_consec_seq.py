class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest_seq = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest_seq = max(length, longest_seq)
        return longest_seq