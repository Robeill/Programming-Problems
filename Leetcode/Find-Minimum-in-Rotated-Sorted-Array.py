class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        lo , hi = -1 , len(nums) - 1
        while lo + 1 < hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] <= nums[len(nums) - 1]:
                hi = mid
            else:
                lo = mid
        return nums[hi]
