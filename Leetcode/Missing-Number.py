class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #one liner
        # return sum(list(range(1, len(nums) + 1))) - sum(nums)
        n = len(nums)
        i = 0
        while i < n:
            curr_idx = nums[i]
            if curr_idx < n and nums[i] != nums[curr_idx]:
                nums[i], nums[curr_idx] = nums[curr_idx], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n