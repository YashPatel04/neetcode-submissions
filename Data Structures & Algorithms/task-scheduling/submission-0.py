class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = Counter(tasks)
        heap = [-c for c in arr.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time+=1
            if heap:
                val = (-heapq.heappop(heap))-1
                if val!=0:
                    queue.append([val, time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(heap, -(queue.popleft()[0]))
        return time
                