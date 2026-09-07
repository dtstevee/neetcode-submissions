# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def depth_calc(root, depth):
            nonlocal max_depth


            if root is None:
                return
            
            # each step, update maximum depth
            max_depth = max(max_depth, depth)

            depth_calc(root.left, depth + 1)
            depth_calc(root.right, depth + 1)
        
        depth_calc(root, 1)
        
        return max_depth
        
        
        
        