from functools import reduce
from typing import List

class Solution:
    # Math
    def missingNumber(self, nums: List[int]) -> int:
        s = reduce(lambda acc,x : acc+x, nums, 0)
        n = len(nums)
        expect = (n*(n+1))//2
        return expect - s

    # Bit manipulation
    def _missingNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n

        for i in range(len(nums)+1):
            result ^= i

        return result
