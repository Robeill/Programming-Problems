class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minimums = [0] * len(nums)
        stack = []
        minimums[0] = nums[0]
        for i in range(1, len(nums)):
            minimums[i] = min(minimums[i - 1], nums[i])
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > minimums[i]:
                while stack and stack[-1] <= minimums[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])

        return False