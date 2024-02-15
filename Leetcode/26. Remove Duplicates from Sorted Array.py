class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = [nums[0]]
        for num in nums[1:]:
            if num != unique[-1]:
                unique.append(num)
        nums[:] = unique 
        return len(unique)