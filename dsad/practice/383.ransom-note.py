#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

import collections

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = collections.Counter(magazine)
        ransomnote_counts = collections.Counter(ransomNote)

        for char, count in ransomnote_counts.items():
            magazine_char_count = magazine_counts[char]
            if magazine_char_count < count:
                return False
        return True
        
# @lc code=end

sol = Solution()
print(sol.canConstruct(ransomNote="leetcode is cool", magazine="close call as fools take sides"))