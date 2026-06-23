class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            x = prices[sell] - prices[buy]
            if x > max_profit:
                max_profit = x

            if prices[buy] < prices[sell]:
                sell += 1
            else:
                buy = sell
                sell += 1

        return max_profit
