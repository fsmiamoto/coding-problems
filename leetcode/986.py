from typing import List

_START = 0
_END = 1

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        if len(firstList) == 0 or len(secondList) == 0:
            return result

        i,j = 0, 0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][_END] < secondList[j][_START]:
                i += 1
                continue
            if secondList[j][_END] < firstList[i][_START]:
                j += 1
                continue

            start = max(firstList[i][_START],secondList[j][_START])
            if firstList[i][_END] <= secondList[j][_END]:
                end = firstList[i][_END]
                i+=1
            else:
                end = secondList[j][_END]
                j+=1

            result.append([start,end])

        return result
