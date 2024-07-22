class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for start in range(n):
            fast, slow, ispos = start, start, nums[start] > 0
            while True:
                if fast == (fast + nums[fast]) % n or nums[fast] * nums[start] <= 0:
                    break
                fast = (fast + nums[fast]) % n
                if fast == (fast + nums[fast]) % n or nums[fast] * nums[start] <= 0:
                    break
                fast = (fast + nums[fast]) % n
                slow = (slow + nums[slow]) % n
                if fast == slow:
                    return True
        return False
