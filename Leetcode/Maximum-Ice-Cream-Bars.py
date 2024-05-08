class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum = 0
        res = 0
        for i in range(len(costs)):
            sum += costs[i]
            if sum <= coins:
                res += 1
            else:
                break
        return res