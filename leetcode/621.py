from heapq import heapify, heappush, heappop
from collections import deque, defaultdict
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      taskCount = defaultdict(int)

      for task in tasks:
        taskCount[task] += 1


      heap = [-count for count in taskCount.values()]
      heapify(heap)

      queue = deque()

      currentTime = 0
      while heap or queue:
        currentTime += 1

        if queue and currentTime > queue[0][0]:
          (_,count) = queue.popleft()
          heappush(heap, count)

        if not heap: continue

        count = heappop(heap)
        count += 1

        if count != 0:
          queue.append((currentTime+n,count))

      return currentTime
