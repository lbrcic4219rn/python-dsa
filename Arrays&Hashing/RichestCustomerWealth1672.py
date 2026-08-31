from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in range(len(accounts)):
            for j in range(1, len(accounts[0])):
                accounts[i][j] += accounts[i][j - 1]

        richest = 0
        for i in range(len(accounts)):
            richest = max(richest, accounts[i][len(accounts[i]) - 1])
        return richest
