class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for l, r, s in bookings:
            res[l-1] += s
            if r < n: res[r] -= s
        for i in range(1, n):
            res[i] += res[i-1]
        return res
