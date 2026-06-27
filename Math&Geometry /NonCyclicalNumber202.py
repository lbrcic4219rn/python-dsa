class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            num = 0
            while n != 0:
                num += (n % 10) ** 2
                n //= 10
            if num in seen:
                return False
            seen.add(num)
            n = num

        return True