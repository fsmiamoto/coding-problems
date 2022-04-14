from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      lower, upper = self._findAverageEatingSpeed(piles,h), max(piles)

      while lower < upper:
        middle = (lower+upper)//2
        if self._isSolution(piles, middle, h):
          upper = middle
        else:
          lower = middle + 1

      return upper

    def _isSolution(self, piles: List[int], k: int, h :int) -> bool:
      return sum([ceil(x/k) for x in piles]) <= h

    def _findAverageEatingSpeed(self, piles: List[int], h: int) -> int:
      return ceil(sum(piles) / h)
