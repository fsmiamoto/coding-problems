START = 0
END = 1
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # mergedInterval = [[1,3],[2,3],[3,4]]
        merged = self.merge(intervals)
        return len(intervals) - len(merged)

    def merge(self, intervals):
      # Sort by starting time
      intervals.sort(key=lambda interval: interval[0])

      start, end = intervals[0][START], intervals[0][END]

      result = []

      for i in range(1, len(intervals)):
        if intervals[i][START] < end:
          end = min(end, intervals[i][END])
        else:
          result.append([start,end])
          start = intervals[i][START]
          end = intervals[i][END]

      result.append([start,end])

      return result
