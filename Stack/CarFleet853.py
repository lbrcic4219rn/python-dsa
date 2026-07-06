from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        startSpeed = []
        for i in range(len(position)):
            startSpeed.append((position[i], speed[i]))

        startSpeed.sort(reverse=True)

        stack = []
        for index, s in startSpeed:
            finishTime = (target - index) / s
            if stack and finishTime <= stack[-1]:
                continue
            stack.append(finishTime)

        return len(stack)
