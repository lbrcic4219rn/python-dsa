class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = ""
            for i in range(0, len(s), k):
                part = s[i: i + k]
                cnt = 0
                for ch in part:
                    cnt += int(ch)
                tmp += str(cnt)
            s = tmp

        return s
