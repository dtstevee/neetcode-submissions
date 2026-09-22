"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {}
        def dfs(node):
            nonlocal hash_map
            if node is None:
                return node
            if node.neighbors is None:
                return node.neighbors
            if node in hash_map:
                return hash_map[node]
            
            copy = Node(node.val)
            hash_map[node] = copy            

            for item in node.neighbors:
                copy.neighbors.append(dfs(item))
            
            return copy
        
        return dfs(node)
                
                