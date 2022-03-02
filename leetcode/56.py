from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        result = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                result.append([start,end])
                start = interval[0]
                end = interval[1]

        result.append([start,end])

        return result
