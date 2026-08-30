from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        currTime = customers[0][0]
        for arrive, time in customers:
            if arrive > currTime:
                currTime = arrive
            currTime += time
            wait += currTime - arrive
        return wait / len(customers)
