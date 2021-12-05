#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root) -> int:

        self.longest_path = 0
        
        def arrow_length(node):
            
            if not node: return 0

            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)

            left_arrow = right_arrow = 0

            if node.left and node.val == node.left.val:
                left_arrow = left_length + 1
            if node.right and node.val == node.right.val:
                right_arrow = right_length + 1

            self.longest_path = max(self.longest_path, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        
        arrow_length(root)
        return self.longest_path

        
# @lc code=end

