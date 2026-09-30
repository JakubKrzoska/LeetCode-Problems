class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        adj = {i:[] for i in range(n)}

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)