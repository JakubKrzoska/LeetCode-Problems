class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((d, w))
            adj[d].append((s, w))

        minHeap = [(0, 0)]
        res = 0 
        visit = set()
        while minHeap and len(visit) < n:
            weight, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            
            visit.add(v)
            res += weight
            for neighbor, w in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (w, neighbor))
        
        return res if len(visit) == n else -1