# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(root, maxi_num):
            nonlocal count
            if root is None:
                return
            
            maxi_num = max(maxi_num, root.val)
            if root.val >= maxi_num:
                count += 1
            
            dfs(root.left, maxi_num)
            dfs(root.right, maxi_num)
        
        dfs(root, float("-inf"))

        return count
        
        