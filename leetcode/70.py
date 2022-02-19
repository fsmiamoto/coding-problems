from typing import Dict

class Solution:
    # Iterative, fibonacci
    def _climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        a, b = 1, 1
        i = 2

        while i <= n:
            a, b = b, a+b
            i += 1

        return b

    # Dynamic Programming
    def climbStairs(self, n:int) -> int:
        return self._climbStairsMemoized(n, {})

    def _climbStairsMemoized(self, n: int, memo: Dict[int, int]):
        m = memo.get(n)
        if m:
            return m

        if n < 2:
            return 1

        oneStepBelow = self._climbStairsMemoized(n-1, memo)
        twoStepsBelow = self._climbStairsMemoized(n-2, memo)

        memo[n-1]= oneStepBelow
        memo[n-2]= twoStepsBelow

        return oneStepBelow + twoStepsBelow
