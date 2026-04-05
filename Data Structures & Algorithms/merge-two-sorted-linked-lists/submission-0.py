class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        ans = None
        if(list1.val < list2.val):
                ans = list1
                list1 = list1.next
        else:
            ans = list2
            list2 = list2.next
        fin = ans
        while list1 != None and list2 != None:
            
            if(list1.val < list2.val):
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        
        ans.next = list1 if list1 else list2
        return fin