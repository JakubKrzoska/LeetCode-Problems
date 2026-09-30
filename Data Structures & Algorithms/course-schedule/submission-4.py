class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        visitedSet = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visitedSet:
                return False
            if preMap[crs] == []:
                return True

            visitedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitedSet.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True

        