class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return False

        adj = {i:[] for i in range(n)}

        visited = set()

        for src, des in edges:
            adj[src].append(des)
            adj[des].append(src)


        def dfs(curr, visited, prev):
            if curr in visited:
                return False

            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, visited, curr):
                    return False
            return True


        return dfs(0, visited, -1) and n == len(visited)       
