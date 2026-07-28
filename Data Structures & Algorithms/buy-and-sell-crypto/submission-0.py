class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =0
        sell =1
        max_profit = 0

        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]

            if current_profit >0:
                max_profit = max(max_profit, current_profit)
            elif prices[sell] < prices[buy] :
                buy = sell
            sell += 1
        return max_profit