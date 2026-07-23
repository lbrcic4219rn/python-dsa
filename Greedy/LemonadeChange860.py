from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #  5, 10
        register = [0, 0]

        for bill in bills:
            if bill == 5:
                register[0] += 1
            elif bill == 10:
                register[0] -= 1
                register[1] += 1
            else:
                if register[1] > 0:
                    register[1] -= 1
                    register[0] -= 1
                else:
                    register[0] -= 3
            if register[0] < 0 or register[1] < 0:
                return False
        return True