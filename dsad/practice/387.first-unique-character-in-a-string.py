#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

import collections

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter_map = collections.Counter(s)
        for index, char in enumerate(s):
            if counter_map[char] <= 1:
                return index
        return -1
        
# @lc code=end

sol = Solution()
print(sol.firstUniqChar(s="leetcode"))
