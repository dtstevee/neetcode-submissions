# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_search(root, sub):
            # if both null, return True
            if not root and not sub:
                return True
            
            if (not root and sub) or (not sub and root):
                return False
            
            if root.val != sub.val:
                return False
            
            return dfs_search(root.left, sub.left) and dfs_search(root.right, sub.right)
        
        if not root:
            return False
        
        if dfs_search(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)