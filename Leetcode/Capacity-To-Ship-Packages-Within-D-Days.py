class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights) - 1 , sum(weights)
        def check(mid):
            day , curr = 1 , mid
            for num in weights:
                if curr - num < 0:
                     day += 1
                     curr = mid
                curr -= num
            return day <= days   

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi
