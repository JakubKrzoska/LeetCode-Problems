class UnionFind:
    
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
        self.num = n

    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x == par_y:
            return False
        if self.ranks[par_x] < self.ranks[par_y]:
            self.parents[par_x] = par_y
            self.ranks[par_y] += self.ranks[par_x]
        else:
            self.parents[par_y] = par_x
            self.ranks[par_x] += self.ranks[par_y]
        self.num -= 1
        return True


    def getNumComponents(self) -> int:
        return self.num
