"""
Given an integer array nums and an integer k, 
return the k most frequent elements. You may 
return the answer in any order.

"""

class Solution:
    def topKFrequent(self, nums, k: int):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


####### Alt Solution ###########
class Solution:
    def topKFrequent(self, nums, k: int):
        freq_elems_hash = {}

        for num in nums:
            freq_elems_hash[num] = 1 + freq_elems_hash.get(num, 0)
        
        freq_elems_hash = dict(sorted(freq_elems_hash.items(), key=lambda item: item[1], reverse=True))

        return list(freq_elems_hash.keys())[:k]