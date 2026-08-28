class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        
        while right < len(prices):
            left_num = prices[left]
            right_num = prices[right]
            temp_profit = right_num - left_num
            
            if temp_profit < 0:
                left = right
                right += 1
                continue
            if temp_profit > max_profit:
                max_profit = temp_profit

            right += 1
        return max_profit
                

                
