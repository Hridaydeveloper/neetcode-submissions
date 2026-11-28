class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            curr_price = prices[i] - min_price
            max_profit = max(curr_price, max_profit)
            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit




        