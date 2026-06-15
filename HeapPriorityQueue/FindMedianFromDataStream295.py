import heapq


class MedianFinder:
    def __init__(self):
        self.numsFist = []
        self.numsSecond = []

    def addNum(self, num: int) -> None:
        if len(self.numsFist) > 0 and num < self.numsFist[0]:
            if len(self.numsFist) > len(self.numsSecond):
                heapq.heappush(self.numsSecond, heapq.heappop_max(self.numsFist))
            heapq.heappush_max(self.numsFist, num)
        elif len(self.numsSecond) and num > self.numsSecond[0]:
            if len(self.numsFist) < len(self.numsSecond):
                heapq.heappush_max(self.numsFist, heapq.heappop(self.numsSecond))
            heapq.heappush(self.numsSecond, num)
        else:
            if len(self.numsFist) < len(self.numsSecond):
                heapq.heappush_max(self.numsFist, num)
            else:
                heapq.heappush(self.numsSecond, num)

    def findMedian(self) -> float:
        if len(self.numsFist) == len(self.numsSecond):
            return (self.numsFist[0] + self.numsSecond[0]) / 2
        elif len(self.numsFist) > len(self.numsSecond):
            return self.numsFist[0]
        else:
            return self.numsSecond[0]
