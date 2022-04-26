class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0

        for i in range(len(s)):
          # Expand, odd length
          left, right = i, i

          while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1

          # Even length
          left, right = i, i+1
          while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1

        return count
