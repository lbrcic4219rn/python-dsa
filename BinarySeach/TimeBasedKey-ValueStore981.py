from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.data[key]
        l, r = 0, len(vals)

        while l < r:
            m = l + (r - l) // 2

            if vals[m][0] <= timestamp:
                l = m + 1
            else:
                r = m

        if l == 0:
            return ""

        return vals[l - 1][1]
