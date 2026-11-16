class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = [points[0]]
        for i in range(1, len(points)):
            # end
            if res[-1][1] >= points[i][0]:
                _, end = res.pop()
                res.append([points[i][0], min(end, points[i][1])])
            else:
                res.append(points[i])

        print(res)
        return len(res)
