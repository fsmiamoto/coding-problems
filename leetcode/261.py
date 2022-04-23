from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree is connected acyclic graph
        # Detect cycles
        # Check if all nodes are connected

        graph = {i: [] for i in range(n)}

        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)

        return self._valid_tree(graph, n)

    def _valid_tree(self, graph, n) -> bool:
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)
        is_connected = len(visited) == n

        if not is_connected:
            return False

        def has_cycle(node, parent, visited):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if has_cycle(neighbor,node, visited):
                        return True
                # Neighbor has been visited and is not the parent, cycle detected
                elif parent != neighbor:
                    return True

            return False

        is_acyclic = not has_cycle(0,-1,set())

        if not is_acyclic:
            return False

        return True
