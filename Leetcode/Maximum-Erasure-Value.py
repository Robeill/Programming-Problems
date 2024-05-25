class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        check = set()
        current_sum = 0
        max_sum = 0
        for right in range(len(nums)):
            while nums[right] in check:
                check.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            check.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        return max_sum