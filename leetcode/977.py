# Squared of sorted array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [ x * x for x in nums ]
        l, r = 0, len(squared)-1
        result = []
        while l < r:
            left, right = squared[l], squared[r]
            if left > right:
                result.append(left)
                l += 1
            else:
                result.append(right)
                r -= 1

        # l = r
        result.append(squared[r])

        return result[::-1]
