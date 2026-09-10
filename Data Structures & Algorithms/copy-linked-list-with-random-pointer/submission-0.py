"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_table = {}
        dummy = Node(0)
        curr = dummy

        head_1 = head
        
        while head_1:
            new_node = Node(head_1.val)
            
            # add to hashmap for future reference
            hash_table[head_1] = new_node
            curr.next = new_node

            # iterate to next list
            curr = curr.next
            head_1 = head_1.next

        hash_table[None] = None

        curr = dummy.next
        head_2 = head
        
        while curr:
            curr.random = hash_table[head_2.random]

            curr = curr.next
            head_2 = head_2.next
        
        return dummy.next

        