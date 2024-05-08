class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart = 0
        res = float('inf')
        sum_val = 0
        for windowEnd in range(len(nums)):
            sum_val += nums[windowEnd]
            while sum_val >= target:
                res = min(res, windowEnd - windowStart + 1)
                sum_val -= nums[windowStart]
                windowStart += 1
        return res if res != float('inf') else 0
