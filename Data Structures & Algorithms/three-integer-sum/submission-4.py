class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                suma = nums[l] + nums[r] + v
                if suma > 0:
                    r -= 1
                elif suma < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res