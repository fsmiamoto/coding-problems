from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      maxProfit = 0
      buy = 0
      for sell in range(1,len(prices)):
        profit = prices[sell] - prices[buy]
        if profit <= 0:
          buy = sell
          continue
        maxProfit = max(maxProfit, profit)

      return maxProfit
