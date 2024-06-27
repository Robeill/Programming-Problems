# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a , b = 1, n
        while a < b:
            k = (a + b) // 2
            if isBadVersion(k):
                b = k
            else:
                a = k + 1
        return a