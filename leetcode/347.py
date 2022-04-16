from heapq import heapify, heappop
from typing import List
from collections import defaultdict

class Solution:
    # Using bucket sort, O(n)
    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = defaultdict(int)
      frequency = [[] for _ in range(len(nums))]

      for n in nums:
        count[n] += 1

      for num in count:
        c = count[num]
        frequency[c-1].append(num)

      result = []
      needToAdd = k

      # Start from end
      for i in range(len(frequency)-1,-1,-1):
        if len(frequency[i]) == 0:
          continue

        # Assuming there's a unique solution, len(frequency[i]) cannot be greater than needToAdd
        # Therefore we can always append the entire thing

        result += frequency[i]
        needToAdd -= len(frequency[i])

        if needToAdd == 0:
          break

      return result

    # Using heap, O(k*lg n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      frequency = defaultdict(int)
      for n in nums:
        frequency[n] += 1

      heap = []
      for num in frequency:
        # Use opposite since the Python's built in heap is a min heap only
        heap.append((-frequency[num], num))

      heapify(heap)

      result = []
      for i in range(k):
        (_, num) = heappop(heap)
        result.append(num)

      return result
