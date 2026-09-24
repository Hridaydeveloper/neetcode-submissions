class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
            min_price = min(min_price, prices[i])
        return max_profit 
        