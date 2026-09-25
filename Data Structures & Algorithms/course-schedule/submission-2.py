class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        
        for course,pre in prerequisites:
            graph[pre].append(course)
        
        checked = set()
        def dfs(node, path):
            # if current node already on path, we find a cycle
            if node in checked:
                return True
            if node in path:
                return False
            
            path.add(node)

            # check all associated neighbor
            for nei in graph[node]:
                if not dfs(nei,path):
                    return False
            
            # backtracking
            path.remove(node)
            checked.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True