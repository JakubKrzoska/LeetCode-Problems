class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1

        res = 20000
        while l <= r:
            mid = (l + r)//2

            print(res)
            if nums[l] > nums[r] and nums[l] <= nums[mid]:
                res = min(res, nums[mid])
                l = mid + 1
            elif nums[l] > nums[r] and nums[l] > nums[mid]:
                res = min(res, nums[mid])
                r = mid - 1
            else:
                return min(res, nums[l]) 
        return res


