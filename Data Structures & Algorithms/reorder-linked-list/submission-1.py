# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        stack = []
        res = head
        orig_head = head
        size = 0
        while head != None:
            size += 1
            stack.append(head)
            head = head.next
        
        i = 0
        temp_orig = orig_head
        while i < (size / 2):
            print(orig_head.val)
            temp = stack.pop()
            print("stack: " + str(temp.val))
            temp_orig = orig_head
            next_node = orig_head.next
            orig_head.next = temp
            temp.next = next_node
            orig_head = next_node
            i += 1
        if(size % 2 == 0):
            temp.next = None
        else:
            temp_orig.next = None
        
        