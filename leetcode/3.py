class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      inWindow = set()
      result = 0
      l, r = 0, 0
      while r < len(s):
        char = s[r]
        while char in inWindow:
          inWindow.remove(s[l])
          l += 1
        inWindow.add(char)
        result = max(result, r-l+1)
        r += 1

      return result
