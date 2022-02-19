from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)

        while left < right:
            middle = (left + right) // 2

            if arr[middle] > arr[middle+1]:
                right = middle
            else:
                left = middle + 1

        return left
