# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs_search(p, q):
            if (p is None and q is not None) or (q is None and p is not None):
                return False

            if p is None and q is None:
                return True
            
            if p.val != q.val:
                return False
            
            left_search = dfs_search(p.left, q.left)
            right_search = dfs_search(p.right, q.right)

            return left_search and right_search
        
        return dfs_search(p,q)