#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        profit = 0

        min_buy = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])

        return profit
        
# @lc code=end

