class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        if k <= numOnes:
            return k

        if k <= numOnes + numZeros:
            return numOnes

        remaining = k - numOnes - numZeros
        return numOnes - remaining