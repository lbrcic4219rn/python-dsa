from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack[-1] > 0 > asteroid:
                if stack[-1] + asteroid > 0:
                    break
                if stack[-1] + asteroid == 0
                    stack.pop()
                    break
                stack.pop()
            else:
                stack.append(asteroid)
        return stack
