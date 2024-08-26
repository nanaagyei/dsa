"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, 
and the sign represents its direction (positive meaning right, 
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.
"""

class Solution:
    def asteroidCollision(self, asteroids: list) -> list:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    asteroid = 0
                    stack.pop()
            
            if asteroid:
                stack.append(asteroid)
        return stack