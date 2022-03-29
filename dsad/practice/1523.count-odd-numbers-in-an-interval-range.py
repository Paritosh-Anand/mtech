#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
from math import ceil


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        # print(f"high % 2 = {high % 2}, low % 2 = {low % 2}")
        t = 1 if (high % 2 > 0 and low % 2 > 0) else 0
        a = high - low
        
        # print(f"a = {a}, ceil(a/2) = {ceil(a/2)}, t = {t}")
        b = ceil(a/2)
        m = t + b
        return m
# @lc code=end

s = Solution().countOdds(8, 18)
