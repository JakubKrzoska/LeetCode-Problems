class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def dfs(i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            elif sum(curr) > target or i >= len(candidates):
                return 
            
            curr.append(candidates[i])
            dfs(i + 1)

            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1)


        dfs(0)

        return res