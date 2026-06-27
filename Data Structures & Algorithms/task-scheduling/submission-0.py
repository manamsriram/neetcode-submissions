class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-count[x] for x in count] # max heap
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time