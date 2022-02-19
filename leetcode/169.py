from typing import List

class Solution:
    def _majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] = count[n] + 1

        return max(count, key=count.get)

    # https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 1
        for n in nums[1:]:
            if count == 0:
                count += 1
                major = n
            elif n == major:
                count += 1
            else:
                count -= 1

        return major

