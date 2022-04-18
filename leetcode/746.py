class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      # len(cost) >= 2
      costToGetTo = [0,0] + [float('inf') for _ in range(len(cost)-1)]

      # Bottom-up
      lastStep = len(cost)+1
      for step in range(2,lastStep):
        costToGetTo[step] = min(cost[step-1]+costToGetTo[step-1],cost[step-2]+costToGetTo[step-2])

      return costToGetTo[lastStep-1]
