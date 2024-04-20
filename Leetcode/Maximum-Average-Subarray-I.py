class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowStart = 0
        sum_val = 0
        res = float(-inf)
        for windowEnd in range(len(nums)):
            sum_val += nums[windowEnd]
            if windowEnd >= k - 1:
                res = max(res , sum_val / k)
                sum_val -= nums[windowStart]
                windowStart += 1
        return res