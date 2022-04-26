class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        resultLeft, resultRight = 0, 0

        maxLen = 0

        for i in range(len(s)):
          # Expand, odd length
          left, right = i, i

          while left >=0 and right < len(s) and s[left] == s[right]:
            length = right-left+1
            if length > maxLen:
              resultLeft = left
              resultRight = right
              maxLen = length
            left -= 1
            right += 1

          # Even length
          left, right = i, i+1
          while left >=0 and right < len(s) and s[left] == s[right]:
            length = right-left+1
            if length > maxLen:
              resultLeft = left
              resultRight = right
              maxLen = length
            left -= 1
            right += 1

        return s[resultLeft:resultRight+1]
