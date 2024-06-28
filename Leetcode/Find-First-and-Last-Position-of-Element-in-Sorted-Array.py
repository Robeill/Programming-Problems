class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstPosition(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        def lastPosition(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] > target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo - 1
        
        def isGreater(num, target):
            return num >= target
        
        def isSmaller(num, target):
            return num < target
        
        first = firstPosition(nums, target)
        last = lastPosition(nums, target)
        if first < len(nums) and nums[first] == target:
            return [first, last]
        else:
            return [-1, -1]