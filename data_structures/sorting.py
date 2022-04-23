from typing import List

def quicksort(nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return []
    l, r = 0, len(nums)
    pivot = nums[(l+r)//2]
    return quicksort([x for x in nums if x < pivot])+ [x for x in nums if x == pivot] + quicksort([x for x in nums if x > pivot])

def mergesort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    def merge(a: List[int], b: List[int]) -> List[int]:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

    middle = len(nums)//2
    left = mergesort(nums[:middle])
    right = mergesort(nums[middle:])
    return merge(left, right)


a = [5,3,5,3,6,2,3,1,2,5,76,0,4,1,24]

assert sorted(a) == quicksort(a)
assert sorted(a) == mergesort(a)
