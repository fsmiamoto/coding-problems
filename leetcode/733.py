from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image

        before = image[sr][sc]
        image[sr][sc] = newColor
        rowCount, colCount = len(image), len(image[0])
        neighbors = self.neighbors(rowCount, colCount, sr,sc)
        for (neighborRow,neighborCol) in neighbors:
            if image[neighborRow][neighborCol] == before:
                self.floodFill(image,neighborRow,neighborCol,newColor)

        return image

    def neighbors(self,height: int, width: int, row: int, col: int) -> List[tuple[int,int]]:
        offsets = [(0,1),(0,-1),(1,0),(-1,0)]
        result = []
        for (rowOffset, colOffset) in offsets:
            neighborRow, neighborCol = row + rowOffset, col+colOffset
            if neighborRow >= 0 and neighborRow < height and neighborCol >= 0 and neighborCol < width:
                result.append((neighborRow,neighborCol))
        return result
