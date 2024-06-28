class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = [-1] * len(nums)
        for j in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    next_greater[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        return next_greater