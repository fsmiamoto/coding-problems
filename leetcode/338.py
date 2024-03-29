from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        offset = 1
        for i in range(1,n+1):
            if offset == i:
                offset *= 2
            result.append(1 + result[i-offset])

        return result
