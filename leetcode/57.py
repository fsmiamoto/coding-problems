from typing import List

_START = 0
_END = 1

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) < 1:
            return [newInterval]

        i = 0
        result = []

        while i < len(intervals) and intervals[i][_END] < newInterval[_START]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][_START] <= newInterval[_END]:
            newInterval[_START] = min(newInterval[_START],intervals[i][_START])
            newInterval[_END] = max(newInterval[_END],intervals[i][_END])
            i+=1


        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i+=1

        return result
