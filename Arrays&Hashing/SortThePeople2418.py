from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = []
        for i in range(len(names)):
            people.append((heights[i], names[i]))

        sortedPeople = sorted(people, reverse=True)
        res = []

        for _, name in sortedPeople:
            res.append(name)
        return res
      
