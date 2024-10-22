"""
Design a class to find the kth largest integer in a stream of values, including duplicates. 
E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

- constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
- int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
Example 1:

Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

Output:
[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5);   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6
"""

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Time complexity: O(nlogk) for constructor and O(logk) for add

# Space complexity: O(k)
if __name__ == "__main__":
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(6))
    print(kthLargest.add(7))
    print(kthLargest.add(8))