class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        profit = 0
        while r < len(prices):
            curr=0
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                curr = prices[r] - prices[l]

                if curr > profit:
                    profit = curr
                r+=1
        return profit