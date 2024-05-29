class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        nums = list(map(int, str(abs(num))))
        if num < 0:
            nums.sort(reverse=True)
            res = "-" + "".join(map(str, nums))
        else:
            nums.sort()
            if nums[0] == 0:
                for i in range(1, len(nums)):
                    if nums[i] != 0:
                        nums[0], nums[i] = nums[i], nums[0]
                        break
            res = "".join(map(str, nums))
        return int(res)
