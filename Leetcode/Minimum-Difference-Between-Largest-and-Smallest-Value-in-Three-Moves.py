class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n >= 4:
            min_diff = float("inf")
            nums.sort()
            window = (n-1)-3
            for i in range(n):
                if i + window >= n:
                    break
                else:
                    min_diff = min(nums[i+window]-nums[i], min_diff)
            return min_diff
        return 0