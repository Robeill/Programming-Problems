class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            sum_of_squares = l ** 2 + r ** 2
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                l += 1
            else:
                r -= 1
        return False
