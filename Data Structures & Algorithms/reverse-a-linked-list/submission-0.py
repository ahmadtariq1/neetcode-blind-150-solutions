# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
        else:
            next_temp = head.next
            prev_temp = head
            head.next = None
            print(head.val)
            while next_temp != None:
                head = next_temp
                next_temp = head.next
                head.next = prev_temp           
                prev_temp = head
                print(head.val)

                
            return head
