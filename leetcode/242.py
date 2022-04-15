class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False

        letterCount = {}

        # Increment count for letters in S
        for letter in s:
          if letter not in letterCount:
            letterCount[letter] = 0
          letterCount[letter] += 1

        for letter in t:
          if letter not in letterCount:
            return False
          letterCount[letter] -= 1

        for count in letterCount.values():
          if count != 0:
            return False

        return True
