#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

from typing import Optional, TreeNode, List

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        output, stack = [], []
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        print(stack)
        
        return output

        
# @lc code=end

