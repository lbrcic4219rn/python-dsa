from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        aGas = sum(gas)
        aCost = sum(cost)
        if aCost > aGas:
            return -1

        curState = 0
        res = 0
        for i in range(len(gas)):
            curState += gas[i] - cost[i]
            if curState < 0:
                res = i + 1
                curState = 0

        return res
