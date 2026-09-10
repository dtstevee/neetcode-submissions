# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = l1
        list_2 = l2
        carry = 0

        # Initiate the list
        dummy = ListNode(0)
        curr = dummy
        while list_1 or list_2 or carry != 0:
            # take out the number
            if list_1:
                val_1 = list_1.val
                list_1 = list_1.next
            else:
                val_1 = 0
            
            if list_2:
                val_2 = list_2.val
                list_2 = list_2.next
            else:
                val_2 = 0

            # Sum up the total, and only keep the num smaller than 10
            total = val_1 + val_2 + carry
            val = total % 10
            
            # for part bigger than 10, keep it to carry and use the next loop
            curr.next = ListNode(val)
            curr = curr.next
            carry = total // 10
        
        return dummy.next
            
            