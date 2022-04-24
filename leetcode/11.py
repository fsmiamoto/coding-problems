class Solution(object):
    def maxArea(self, heights):
      maxArea = 0
      left, right = 0, len(heights)-1
      while left < right:
        area = min(heights[left],heights[right]) * abs(left-right)
        maxArea = max(area,maxArea)

        # Update the smallest one
        if heights[left] < heights[right]:
          left += 1
        else:
          right -= 1

      return maxArea

    def _maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """

        maxArea = 0
        # O(n^2)
        for i in range(len(heights)):
          for j in range(len(heights)):
            if i == j:
              # Skip itself
              continue
            area = min(heights[i],heights[j]) * abs(i-j)
            maxArea = max(area, maxArea)

        return maxArea
