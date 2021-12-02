# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 or list2 and list1.val > list2.val:
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
        
l1 = [1,2,4]
l2 = [1,3,4]

def insert(root, item):
    temp = ListNode(item)
     
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
     
    return root

def display(root):
    while (root != None) :
        print(root.val, end = " ")
        root = root.next
    print("display done", end="\n")

list1 = None
for i in l1:
    list1 = insert(list1, i)

display(list1)

list2 = None
for i in l2:
    list2 = insert(list2, i)

display(list2)
print("===========")
sol = Solution()
print(display(sol.mergeTwoLists(list1=list1, list2=list2)))



