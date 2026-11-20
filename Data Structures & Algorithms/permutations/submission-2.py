class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for per in perms:
                for i in range(len(per) + 1):
                    per_copy = per.copy()
                    per_copy.insert(i, n)
                    new_perms.append(per_copy)
            perms = new_perms
        
        return perms