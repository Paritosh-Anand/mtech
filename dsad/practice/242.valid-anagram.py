#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
import collections

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = collections.Counter(s)
        t_chars = collections.Counter(t)

        return s_chars == t_chars
        
# @lc code=end

sol = Solution()
print(sol.isAnagram(s='anagram', t='nagaram'))
print(sol.isAnagram(s='rat', t='car'))