#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        data = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in s:
            if i in data.keys():
                stack.append(i)
            elif len(stack) == 0 or i != data[stack.pop()]:
                return False

        return len(stack) == 0

        
# @lc code=end

