class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum_profit = 0
        
        for i in range(len(prices) - 1):
            p1 = prices[i]
            p2 = prices[i + 1]
            diff = p2 - p1
            sum_profit += max(diff, 0)
        return sum_profit