class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        if ones == 0 or ones == len(nums):
            return 0
        cur_ones = 0
        for i in range(ones):
            cur_ones += nums[i]
        res = cur_ones
        for i in range(len(nums)):
            cur_ones -= nums[i]
            cur_ones += nums[(i + ones) % len(nums)]
            res = max(res , cur_ones)
        return ones - res
