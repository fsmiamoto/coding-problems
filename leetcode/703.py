from typing import List
from heapq import heapify, heappop, heappush

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
      self.k = k
      # Python's built Heap is a MinHeap already
      self.min_heap = nums.copy()
      heapify(self.min_heap)
      self.__trim_heap()

    def add(self, val: int) -> int:
      heappush(self.min_heap, val)
      self.__trim_heap()
      return self.min_heap[0]

    def __trim_heap(self):
      while len(self.min_heap) > self.k:
        heappop(self.min_heap)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
