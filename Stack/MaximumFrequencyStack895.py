from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.counts = defaultdict(int)
        self.stacks = defaultdict(list)
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        self.stacks[self.counts[val]].append(val)
        self.maxCount = max(self.maxCount, self.counts[val])

    def pop(self) -> int:
        val = self.stacks[self.maxCount].pop()
        self.counts[val] -= 1
        if not self.stacks[self.maxCount]: self.maxCount -= 1
        return val
