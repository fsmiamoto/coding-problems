from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        matrix = []
        for row in range(m):
            start= row*n
            end = start + n
            matrix.append(original[start:end])

        return matrix
