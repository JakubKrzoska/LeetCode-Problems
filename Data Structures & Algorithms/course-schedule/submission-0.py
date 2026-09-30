class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for cour, pre in prerequisites:
            adj[cour].append(pre)

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            elif adj[course] == []:
                return True
            
            visited.add(course)
            for pre in adj[course]:
                if not dfs(pre): return False
            adj[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True