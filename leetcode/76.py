class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        left, right = 0, 0

        tCount = {}
        for c in t:
          tCount[c] = 1 + tCount.get(c,0)

        currWindowCount, count = {}, 0
        solLeft, solRight = None, None
        while right < len(s):
          letter = s[right]

          if letter not in tCount:
            right += 1
            continue

          currWindowCount[letter] = currWindowCount.get(letter,0) + 1

          if currWindowCount[letter] == tCount[letter]:
            count += 1

          # O(m+t)
          while count == len(tCount):
            if solLeft is None or solRight is None:
                solLeft = left
                solRight = right
            elif (solRight-solLeft+1) > (right-left+1):
                # Update solution, if better than current one
                solLeft = left
                solRight = right

            # Shrink window until it is no longer valid
            if s[left] in currWindowCount:
              if currWindowCount[s[left]] == tCount[s[left]]:
                count -= 1
              currWindowCount[s[left]] -= 1
              if currWindowCount[s[left]] == 0:
                del currWindowCount[s[left]]
            left += 1

          right += 1

        # No solution found
        if solLeft is None or solRight is None:
          return ""

        return s[solLeft:solRight+1]
