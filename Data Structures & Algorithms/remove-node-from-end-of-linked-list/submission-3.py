# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp_orig = head
        size = 0
        while temp_orig != None:
            size += 1
            temp_orig = temp_orig.next
        
        if( n > size):
            return head
        
        index = size - n
        print("index" + str(index))
        temp_orig = head
        
        for i in range(index):
            print(i)
            prev_node = temp_orig
            temp_orig = temp_orig.next
        if(index == 0 and size == 1):
            return None
        elif(index == 0):
            head = temp_orig.next
        else:
            if(temp_orig.next == None):
                prev_node.next = None
            else:
                prev_node.next = temp_orig.next

        return head