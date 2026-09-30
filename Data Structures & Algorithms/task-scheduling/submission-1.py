class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        maxHeap = [-x for x in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1
            if maxHeap:
                value = 1 + heapq.heappop(maxHeap)
                if value:
                    queue.append([value, time + n])
            
            if queue:
                if queue[0][1] == time:
                    value = queue.popleft()[0]
                    heapq.heappush(maxHeap, value)

        return time
