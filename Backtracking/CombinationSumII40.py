class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, currSeq, currTarget):
            if currTarget == 0:
                res.append(currSeq.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > currTarget:
                    break
                currSeq.append(candidates[j])
                backtrack(j + 1, currSeq, currTarget - candidates[j])
                currSeq.pop()

        backtrack(0, [], target)
        return res
