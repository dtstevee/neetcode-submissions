# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def dfs_search(root):
            nonlocal max_depth
            if root is None:
                return 0
            
            left_node = dfs_search(root.left)
            right_node = dfs_search(root.right)

            max_depth = max(max_depth, left_node + right_node)

            return 1 + max(left_node, right_node)
        
        dfs_search(root)

        return max_depth
            