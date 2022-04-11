from typing import List
from heapq import heapify, heappop, heappush

# [] -> 0
# [x] -> x
# [x, x] -> [] -> 0
# [x, y] x < y -> [y-x] -> y-x

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
          return 0

        # We want a max heap and since Python's builtin heap is a min heap,
        # we'll use their opposites
        stones = [-s for s in stones]

        heapify(stones)

        while len(stones) > 1:
          # Negate since we're using opposite values
          first = -heappop(stones)
          second = -heappop(stones)

          if first == second:
            continue

          # Invariant: First is greater than second, thefore first-second is strictly positive
          heappush(stones, -(first-second))

        return -stones[0] if len(stones) > 0 else 0
