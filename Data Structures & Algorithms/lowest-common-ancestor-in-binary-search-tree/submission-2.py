# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if touch the ground, return -1 indicate impossible
        if root is None:
            return -1
        
        p_val = p.val
        q_val = q.val
        root_val = root.val


        # if both p and q smaller than root, then search the left side
        if p_val < root_val and q_val < root_val:
            root = self.lowestCommonAncestor(root.left, p, q)
        
        # if both p and q are larger, search the right side
        elif p_val > root_val and q_val > root_val:
            root = self.lowestCommonAncestor(root.right, p, q)
        
        # otherwise, it has to be the root
        else:
            root = root
        
        return root
            