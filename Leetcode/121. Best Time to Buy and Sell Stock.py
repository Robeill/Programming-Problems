class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left , right = 0 , 1
        max_profit  = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(prices[right] - prices[left] , max_profit)  
            else:
                # We shift the left Pointer to the new minimum number found
                left = right
            right += 1         
        return max_profit
