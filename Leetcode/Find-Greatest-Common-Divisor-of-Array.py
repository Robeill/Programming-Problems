class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b , a % b)
        nums.sort()
        return gcd(nums[0] , nums[-1])