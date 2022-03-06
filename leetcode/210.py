from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
