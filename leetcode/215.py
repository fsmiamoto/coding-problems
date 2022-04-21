from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use opposite values since it's a min heap
        nums = [-n for n in nums]
        heapify(nums)

        # O(n) + O(k*lgn)

        for _ in range(k-1):
            heappop(nums)


        return -heappop(nums)
