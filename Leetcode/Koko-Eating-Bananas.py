class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(nums , idx , max_hours):
            time = 0
            for i in range(len(nums)):
                time += ceil(piles[i] / idx)
            if time > max_hours:
                return False
            else:
                return True
        lo , hi = 0, max(piles)
        while lo + 1 < hi:
            mid = lo + ((hi - lo) // 2)
            if canFinish(piles , mid , h):
                hi = mid
            else:
                lo = mid
        return hi