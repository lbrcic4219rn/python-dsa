from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            match log:
                case "../":
                    if stack:
                        stack.pop()
                case "./":
                    continue
                case _:
                    stack.append(log)
        return len(stack)
