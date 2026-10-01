class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n: return False
        
        adj = {i:[] for i in range(n)}

        for src, dec in edges:
            adj[src].append(dec)
            adj[dec].append(src)

        visited = set()
        res = 0

        def bfs(i):
            visited.add(i)
            q = deque()
            q.append(i)

            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in visited:
                        continue
                    q.append(nei)
                    visited.add(nei)

        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        
        return res
