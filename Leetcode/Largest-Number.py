class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            s1, s2 = str(a) + str(b), str(b) + str(a)
            return 1 if s1 > s2 else -1 if s1 < s2 else 0
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)
        result = ''.join(nums)
        return '0' if result[0] == '0' else result