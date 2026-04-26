class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n = len(prices)
        if n < 2:
            return 0
        
        buy_time = prices[0]
 
        max_profit = 0
        
        for price in prices[1:]:
            profit = price - buy_time
            if profit > max_profit:
                max_profit =  profit
            if price < buy_time:
                buy_time = price
        return max_profit
    
    
   