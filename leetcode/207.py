from collections import deque, defaultdict
from typing import List

class Solution:
    # Cycle detection
    def canFinish(self, numCourses:int, prerequisites: List[List[int]]) -> bool:
      # Build a Graph
      # Traverse the graph using DFS
      # If a cycle is detected, return False

      graph = defaultdict(list)

      for [before,after] in prerequisites:
        graph[after].append(before)

      visited, stack = set(), set()

      def hasCycle(node, graph, visited, stack) -> bool:
        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
          if neighbor not in visited:
            if hasCycle(neighbor, graph, visited, stack):
              return True
          elif neighbor in stack:
            return True

        stack.remove(node)

        return False

      for course in range(numCourses):
        if course not in visited:
          if hasCycle(course, graph, visited, stack):
            return False

      return True

    # Topo sort, kinda wasteful though
    def _canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      if len(prerequisites) < 2:
        return True

      graph = {i: [] for i in range(numCourses)}
      dependencies = {i: 0 for i in range(numCourses)}

      for prereq in prerequisites:
        before, after = prereq[0], prereq[1]
        graph[before].append(after)
        dependencies[after] += 1

      courseQueue = deque()
      for course in dependencies:
        if dependencies[course] == 0:
          courseQueue.append(course)

      topoSort = []
      while courseQueue:
        course = courseQueue.popleft()
        topoSort.append(course)
        for dep in graph[course]:
          dependencies[dep] -= 1
          if dependencies[dep] == 0:
            # No more deps, we can take this course now
            courseQueue.append(dep)

      return len(topoSort) == numCourses
