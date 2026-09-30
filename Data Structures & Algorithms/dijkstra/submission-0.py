class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((w, d))
        
        shortest = {}
        minHeap = [(0, src)]
        while minHeap:
            w1, d1 = heapq.heappop(minHeap)
            if d1 in shortest:
                continue
            shortest[d1] = w1

            for w2, d2 in adj[d1]:
                if d2 not in shortest:
                    heapq.heappush(minHeap, (w2+ w1, d2))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest


