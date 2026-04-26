class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n = len(prices)
        if n < 2:
            return 0
        
        buy_time = prices[0]
 
        sell_time = 0
        
        for price in prices[1:]:
            profit = price - buy_time
            if profit > sell_time:
                sell_time =  profit
            if price < buy_time:
                buy_time = price
        return sell_time
    
    
   