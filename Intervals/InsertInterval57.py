from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (start, end) in enumerate(intervals):
            newStart, newEnd = newInterval

            if newEnd < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newStart:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(start, newStart),
                    max(end, newEnd)
                ]
        res.append(newInterval)
        return res
