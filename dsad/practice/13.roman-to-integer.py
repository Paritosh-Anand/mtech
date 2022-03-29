#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def __init__(self):
        self.ordered_letter = ["I","V","X","L","C","D","M"]
        self.letter_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,    
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        ans = 0
        s_len = len(s)
        for i, j in enumerate(s):
            print(f"i: {i}, j: {j}, letter_to_int: {self.letter_to_int.get(j)}")
            if i+1 < s_len and self.letter_to_int.get(s[i]) < self.letter_to_int.get(s[i+1]):
                ans -= self.letter_to_int.get(j)
            else:
                ans += self.letter_to_int.get(j)
        return ans
        
# @lc code=end

sol = Solution()
ans = sol.romanToInt(s="MCMXCIV")
print(f"ans: {ans}")

