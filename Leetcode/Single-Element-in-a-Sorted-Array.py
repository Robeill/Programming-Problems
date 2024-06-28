class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def isSide(num , idx):
            if idx % 2 == 0:
                return num[idx] != num[idx + 1]
            else:
                return num[idx] != num[idx - 1]
        lo , hi = - 1, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + ((hi - lo) // 2)
            if isSide(nums , mid):
                hi = mid
            else:
                lo = mid
        return nums[hi]