class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mindiff = float('inf')
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return target
                else:
                    diff = abs(target - sum)
                    if diff < mindiff:
                        mindiff = diff
                        ans = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
        return ans