class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isGreater(num , index):
            if index == len(num) - 1:
                return True
            return num[index] > num[index + 1]

        lo, hi = -1, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if isGreater(nums, mid):
                hi = mid
            else:
                lo = mid
        return hi