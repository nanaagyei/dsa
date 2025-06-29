"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.


Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""

import heapq


def longestDiverseString(a: int, b: int, c: int) -> str:
    pq = []
    if a > 0:
        heapq.heappush(pq, (-a, "a"))
    if b > 0:
        heapq.heappush(pq, (-b, "b"))
    if c > 0:
        heapq.heappush(pq, (-c, "c"))

    result = []
    while pq:
        count, character = heapq.heappop(pq)
        count = -count
        if (len(result) >= 2 and result[-1] == character and result[-2] == character):
            if not pq:
                break
            tempCount, tempChar = heapq.heappop(pq)
            result.append(tempChar)
            if tempCount + 1 < 0:
                heapq.heappush(pq, (tempCount + 1, tempChar))
            heapq.heappush(pq, (-count, character))
        else:
            count -= 1
            result.append(character)
            if count > 0:
                heapq.heappush(pq, (-count, character))
    return "".join(result)


if __name__ == "__main__":
    a = 1
    b = 1
    c = 7
    print(longestDiverseString(a, b, c))
