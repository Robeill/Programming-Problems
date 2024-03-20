class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1
        while n * i % 2 != 0:
            i += 1
        return n * i