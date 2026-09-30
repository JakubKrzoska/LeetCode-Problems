class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
        self.n = n
    
    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    
    def union(self, x1, x2):
        par1, par2 = self.find(x1), self.find(x2)
        if par1 != par2:
            if self.ranks[par1] < self.ranks[par2]:
                self.parents[par1] = par2
                self.ranks[par2] += self.ranks[par1]
            else:
                self.parents[par2] = par1
                self.ranks[par1] += self.ranks[par1]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for n1, n2, w in edges:
            heapq.heappush(minHeap, (w, n1, n2))

        uf = UnionFind(n)
        components = n
        res = 0

        while minHeap and components > 1:
            w, n1, n2 = heapq.heappop(minHeap)
            if uf.union(n1, n2):
                res += w
                components -= 1
        
        return res if components == 1 else -1








