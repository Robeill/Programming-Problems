class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeated = 0
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                repeated = abs(num)
            else:
                nums[index] *= -1
        missing = 0
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break
        return [repeated, missing]