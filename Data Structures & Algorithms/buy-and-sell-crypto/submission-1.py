# need to know the best price only, so we get the lowest price and compare with the most best price by using i
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0] # first day of buy price
        best_price = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            current_price = prices[i] - lowest_price
            best_price = max(best_price,current_price)
        return best_price

                

        
        