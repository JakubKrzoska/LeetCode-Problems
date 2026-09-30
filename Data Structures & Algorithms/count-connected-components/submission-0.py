class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        visited = set()
        res = 0

        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            for nei in adj[i]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res