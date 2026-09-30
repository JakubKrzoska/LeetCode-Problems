class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[-1] <= nums[mid] >= nums[0]:
                l = mid + 1
            elif nums[0] >= nums[mid] <= nums[-1] or nums[mid] >= nums[0]:
                r = mid - 1
        
        return nums[l]
