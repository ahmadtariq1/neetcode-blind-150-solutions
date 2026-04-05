# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        check = False
        
        while not check and head != None:
            if(head.val == "x"):
                check  = True
            head.val = "x"
            head = head.next
        
        return check
