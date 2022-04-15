from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # k = max string length
        # n*(k*log(k)) to sort the array of words

        # 1. Sort each string into a separate array
        # ["eat", "tea", "tan", "ate", "nat", "bat"]
        # ["aet", "aet", "ant", "aet", "ant", "abt"]
        # 2. Traverse array with sorted strings, add values to hashmap
        # {"aet": [0,1,3], "ant": [2, 4], "abt": [5]}
        # 3. Build result from hash map
        # result = [["eat", "tea", "ate"], ...]

        sortedWords = [''.join(sorted(s)) for s in strs]

        groups = {}
        for (index,word) in enumerate(sortedWords):
          if word not in groups:
            groups[word] = []
          groups[word].append(index)

        result = []
        for group in groups:
          groupWords = []
          for i in groups[group]:
            groupWords.append(strs[i])
          result.append(groupWords)

        return result
