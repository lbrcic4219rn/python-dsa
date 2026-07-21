class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            first = 1 if i >= 0 and a[i] == "1" else 0
            second = 1 if j >= 0 and b[j] == "1" else 0

            num = first + second + carry

            res.append(num % 2)
            carry = num // 2
            i -= 1
            j -= 1

        return "".join(map(str, reversed(res)))
