from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n

        while left < right:
            middle = (left + right) // 2

            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle

        return letters[left % n]
