class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1]*n

        def find(n):
            res = n
            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if ranks[p2] > ranks[p1]:
                ranks[p2] += ranks[p1]
                parents[p1] = parents[p2]
            else:
                ranks[p1] += ranks[p2]
                parents[p2] = parents[p1]

            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

