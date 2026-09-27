class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        min_price=prices[0]
        for i in range(len(prices)):
            if min_price>prices[i]:
                min_price=prices[i]
            if profit<prices[i]-min_price:    
                profit=prices[i]-min_price
        return profit