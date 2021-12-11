#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import Optional, List

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])

        return dp[0][-1]

        
# @lc code=end

