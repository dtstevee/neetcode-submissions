# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val_list = []
        def dfs(root, k,val_list):
            if root is None:
                return
            
            dfs(root.left, k, val_list)
            val_list.append(root.val)
            dfs(root.right, k, val_list)
        
        dfs(root, k, val_list)
        
        return val_list[k-1]
        
        