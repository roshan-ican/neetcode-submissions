class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        r = 1

        for l in range(len(prices) - 1):
            if prices[l] < prices[r]:
                buy = prices[r] - prices[l]
                profits.append(buy)
                
            r+=1
        return sum(profits) 