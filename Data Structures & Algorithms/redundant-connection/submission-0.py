class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        ranks = [1]*(len(edges)+1)


        def find(n):
            while n != par[n]:
                n = par[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if ranks[p1] >= ranks[p2]:
                ranks[p1] += ranks[p2]
                par[p2] = p1
            else:
                ranks[p2] += ranks[p1]
                par[p1] = p2

            return True
        
        for s, e in edges:
            if not union(s, e):
                return [s, e]