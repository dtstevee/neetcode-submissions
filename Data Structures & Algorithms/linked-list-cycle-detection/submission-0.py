# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()
        cur = head

        while cur:
            if cur in hash_set:
                return True

            hash_set.add(cur)
            cur = cur.next
        
        return False