class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        dic = {}
        for a, b in paths:
            dic[a] = b

        city = list(dic)[0]
        while city in dic:
            city = dic[city]

        return city
