class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let lowest = prices[0]
        let maxProfit = 0

        for(let i =0; i < prices.length; i++){
            if(prices[i] <= lowest){
                lowest = prices[i]
            }
            let currPrice = prices[i]
            let sellPrice = currPrice - lowest
            if(sellPrice > maxProfit){
                maxProfit = sellPrice 
            }

        }
        if(maxProfit === 0){
            return 0
        }
        return maxProfit
    
    }
}
