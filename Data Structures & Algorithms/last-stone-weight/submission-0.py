class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)
        
        while len(maxHeap) > 1:
            stone1, stone2 = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            newWei = -stone1 - (-stone2)
            if newWei > 0:
                heapq.heappush(maxHeap, -newWei)
        if maxHeap:
            return -heapq.heappop(maxHeap)
        else:
            return 0
