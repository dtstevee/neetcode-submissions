class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        checked = set()
        result = []
        def dfs(node, path):
            if node in checked:
                return True
            if node in path:
                return False
            path.add(node)
            
            for nei in graph[node]:
                if not dfs(nei,path):
                    return False
            
            path.remove(node)
            checked.add(node)
            result.append(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        result.reverse()

        return result