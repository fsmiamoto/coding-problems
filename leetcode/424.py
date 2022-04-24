from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)

        left, right = 0, 0
        maxFreq, maxLen = 0, 0
        while right < len(s):
          count[s[right]] += 1
          maxFreq = max(maxFreq, count[s[right]])

          # windowLen = right-left+1
          while (right-left+1) - maxFreq > k:
            count[s[left]] -= 1
            left += 1

          maxLen = max(maxLen, right-left+1)
          right += 1

        return maxLen
