from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [nums[0]]
        for i in range(1,len(nums)):
            self.sums.append(self.sums[i-1]+nums[i])


    # sums[n] = sums[n-1] + nums[n] -> nums[n] = sums[n] - sums[n-1]
    # nums[n] = sums[n] - sums[n-1]
    # nums[n-1] = sums[n-1] - sums[n-2]
    # nums[n-2] = sums[n-2] - sums[n-3]
    # ...
    # nums[n-m] = sums[n-m] - sums[n-m-1]
    # nums[n] + ... + nums[n-m] = sums[n] - sums[n-m-1]
    # left = n-m
    # right = n
    # result = sums[right] -sums[left-1]


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
