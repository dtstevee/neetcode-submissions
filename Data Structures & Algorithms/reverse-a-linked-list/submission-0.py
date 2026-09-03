# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            # record next node
            next_node = current.next

            # update linked list
            current.next = prev

            # update prev
            prev = current
            current = next_node
        return prev