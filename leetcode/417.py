class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        canReachPacific, canReachAtlantic = set(), set()

        def valid(row: int, col: int) -> bool:
            return row >= 0 and row < ROWS and col >= 0 and col < COLS

        def dfs(row: int, col: int, visited, prevHeight: int):
            if (row,col) in visited or not valid(row,col) or prevHeight > heights[row][col]:
                return

            h = heights[row][col]
            visited.add((row,col))
            dfs(row+1,col,visited,h)
            dfs(row-1,col,visited,h)
            dfs(row,col+1,visited,h)
            dfs(row,col-1,visited,h)

        # Instead of running the algorithm from each position, get position can be reached from both
        # pacific and atlantic
        for c in range(COLS):
            dfs(0,c, canReachPacific, heights[0][c])
            dfs(ROWS-1,c, canReachAtlantic, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0, canReachPacific, heights[r][0])
            dfs(r,COLS-1, canReachAtlantic, heights[r][COLS-1])

        # Get intersection
        return list(canReachAtlantic.intersection(canReachPacific))

    # Naive, my first solution
    def _pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def valid(row: int, col: int) -> bool:
            return row >= 0 and row < ROWS and col >= 0 and col < COLS

        def canReachPacific(row, col,visited) -> bool:
            if not valid(row,col) or (row,col) in visited:
                return False

            if row == 0 or col == 0:
                return True

            visited.add((row,col))

            for (x,y) in [(0,1), (0,-1),(1,0),(-1,0)]:
                neighborRow, neighborCol = row+x, col+y
                if not valid(neighborRow, neighborCol):
                    continue

                if heights[row][col] >= heights[neighborRow][neighborCol]:
                    if canReachPacific(neighborRow, neighborCol,visited):
                        return True

            return False

        def canReachAtlantic(row, col, visited) -> bool:
            if not valid(row,col) or (row,col) in visited:
                return False

            if row == ROWS-1 or col == COLS-1:
                return True

            visited.add((row,col))

            for (x,y) in [(0,1), (0,-1),(1,0),(-1,0)]:
                neighborRow, neighborCol = row+x, col+y
                if not valid(neighborRow, neighborCol):
                    continue

                if heights[row][col] >= heights[neighborRow][neighborCol]:
                    if canReachAtlantic(neighborRow, neighborCol,visited):
                        return True

            return False


        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if canReachPacific(row,col,set()) and canReachAtlantic(row,col,set()):
                    result.append([row,col])

        return result

