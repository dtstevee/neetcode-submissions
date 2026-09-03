# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2
        
        dummy = ListNode()
        prev = dummy
        
        while cur_1 and cur_2:
            if cur_1.val <= cur_2.val:
                prev.next = cur_1
                prev = cur_1
                cur_1 = cur_1.next

            else:
                prev.next = cur_2
                prev = cur_2
                cur_2 = cur_2.next
        
        prev.next = cur_1 or cur_2

        return dummy.next       