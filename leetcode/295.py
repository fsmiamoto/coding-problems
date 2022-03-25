from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        self._balanceHeaps()


    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            # Safe to index both heaps considering our invariant
            return self._avg(-self.maxHeap[0], self.minHeap[0])

        return float(-self.maxHeap[0])


    def _avg(self, a: int,  b: int) -> float:
        return (a+b) / 2.0

    def _balanceHeaps(self) -> None:
        # Invariant: Both heaps will have the same number of elements
        # OR the max heap has one more element
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
