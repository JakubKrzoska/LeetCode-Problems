class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims algorithm
        adj = {i: [] for i in range(len(points))}
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        visited = set()
        minHeap = [(0, 0)]
        res = 0

        while len(visited) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            visited.add(point)
            res += cost

            for cost2, point2 in adj[point]:
                if point2 not in visited:
                    heapq.heappush(minHeap, (cost2, point2))
        return res

