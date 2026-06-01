from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            key = [0] * 26
            for i in range(len(str)):
                key[ord(str[i]) - ord('a')] += 1
            res[tuple(key)].append(str)


        return list(res.values())