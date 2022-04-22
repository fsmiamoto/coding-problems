class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.isEnd = True
            return

        firstLetter, rest = word[0], word[1:]
        if firstLetter not in self.children:
            self.children[firstLetter] = Node()

        self.children[firstLetter].insert(rest)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        self.wordsToFind = len(words)

        trie = Node()
        for w in words:
            trie.insert(w)

        result, visited = set(), set()

        def valid(row: int, col: int) -> bool:
            return row >= 0 and row < m and col >= 0 and col < n

        def search(row: int, col: int, prefix: str, node: 'Node'):
            if self.wordsToFind == 0:
                return

            if not valid(row,col) or (row, col) in visited:
                return

            word = prefix + board[row][col]

            letter = board[row][col]

            if letter not in node.children:
                return

            node = node.children[letter]

            if node.isEnd:
                self.wordsToFind -= 1
                # Don't check this word again
                node.isEnd = False
                result.add(word)

            visited.add((row,col))

            search(row+1,col,word,node)
            search(row-1,col,word,node)
            search(row,col+1,word,node)
            search(row,col-1,word,node)

            visited.remove((row,col))

        for i in range(m):
            for j in range(n):
                search(i,j,'', trie)

        return list(result)

