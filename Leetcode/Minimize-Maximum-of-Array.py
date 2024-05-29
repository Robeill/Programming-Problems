class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        max_value = 0
        for i in range(len(nums)):
            total += nums[i]
            max_value = max(max_value, (total + i) // (i + 1))
        return max_value