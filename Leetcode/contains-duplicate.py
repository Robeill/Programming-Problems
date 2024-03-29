class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #It has a time complexity of O(nlogn) and space complexity of O(1)
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
               return True
        return False