from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            middle = (right + left) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        # left == right
        # assert left == right

        if nums[left] == target:
            return left

        return -1
