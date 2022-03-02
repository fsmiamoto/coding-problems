class Solution:
    # This is pretty ugly
    def checkInclusion(self, pattern: str, _str: str) -> bool:
      patternDict = {}
      patternTotal = len(pattern)
      for c in pattern:
        if c not in patternDict:
          patternDict[c] = 0
        patternDict[c] += 1

      start, end = 0, 0
      strDict, strTotal = {}, 0
      result = False
      while end < len(_str):
        char = _str[end]
        print(strDict)

        if char not in patternDict:
          # Start again
          start = end+1
          end = start
          strDict = {}
          strTotal = 0
          continue

        if char not in strDict:
          strDict[char] = 0
        else:
          while strDict[char] == patternDict[char]:
            strDict[_str[start]] -= 1
            start += 1
            strTotal -= 1

        strDict[char] += 1
        strTotal += 1
        if strTotal == patternTotal:
          result = True
          break

        end += 1

      return result
