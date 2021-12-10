#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        tmp = ListNode(0)
        tmp.next = head

        prev, curr = tmp, head
        while curr:
            print(prev.val, curr.val)
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next
        
        return tmp.next
                
# @lc code=end



