class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        best_profit = 0
        
        for i in range(1,len(prices)):
            if prices[i]<lowest_buy:
                lowest_buy = prices[i]  
            current_profit = prices[i] - lowest_buy
            best_profit = max(best_profit,current_profit)
        return best_profit

        