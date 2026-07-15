from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
                continue
            if o == "C":
                stack.pop()
                continue
            if o == "D":
                stack.append(stack[-1] * 2)
                continue
            stack.append(int(o))

        return sum(stack)
