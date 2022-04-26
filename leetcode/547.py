class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        # Union find
        numOfNodes = len(isConnected)

        parent = [i for i in range(numOfNodes)]
        rank = [1] * numOfNodes

        def findParent(node):
          if parent[node] != node:
            parent[node] = findParent(parent[node])
          return parent[node]

        def union(a,b):
          parentA, parentB = findParent(a), findParent(b)

          if parentA == parentB:
            return 0

          if rank[parentA] > rank[parentB]:
            parent[parentB] = parentA
            rank[parentA] += rank[parentB]
          else:
            parent[parentA] = parentB
            rank[parentB] += rank[parentA]

          return 1

        numOfComponents = numOfNodes

        seen = set()
        for a in range(numOfNodes):
          for b in range(numOfNodes):
            if (b,a) in seen or isConnected[a][b] == 0:
              continue

            numOfComponents -= union(a,b)
            seen.add((a,b))

        return numOfComponents
