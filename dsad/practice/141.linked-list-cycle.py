#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionSpaceOn:
    def hasCycle(self, head: ListNode) -> bool:

        # Time Complexity O(n), Space Complexity O(n)
        visited = set()
        while(head and head not in visited):
            visited.add(head)
            head = head.next
        return True


# @lc code=start
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None or head.next is None: return False
        slow = head
        fast = head.next
        
        # Time Complexity O(n), Space Complexity O(1)
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        
# @lc code=end


