class NumArray:

    def __init__(self, nums: List[int]):
        self.pfs = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pfs[i + 1] = self.pfs[i] + nums[i]

    def sumRange(self, l: int, r: int) -> int:
        return self.pfs[r + 1] - self.pfs[l]
