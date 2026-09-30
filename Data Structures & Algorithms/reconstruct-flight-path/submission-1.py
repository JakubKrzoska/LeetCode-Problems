class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort()

        for s, d in tickets:
            if s not in adj:
                adj[s] = []
            adj[s].append(d)

        res = ["JFK"]

        def backtrack(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for index, city in enumerate(temp):
                adj[src].pop(index)
                res.append(city)

                if backtrack(city):
                    return True

                adj[src].insert(index, city)
                res.pop()
            return False

        backtrack("JFK")
        return res


            