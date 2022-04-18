from math import sqrt
from heapq import heappush, heappop
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      def distanceToOrigin(x,y):
        return sqrt(x**2 + y**2)

      heap = []
      for [x,y] in points:
        distance = distanceToOrigin(x,y)
        heappush(heap, (distance,x,y))

      result = []
      for _ in range(k):
        (_,x,y) = heappop(heap)
        result.append([x,y])

      return result
