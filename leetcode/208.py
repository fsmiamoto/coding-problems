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

    def search(self, word: str, isEntireMatch = True) -> bool:
      if len(word) == 0:
        return self.isEnd or not isEntireMatch

      firstLetter, rest = word[0], word[1:]
      if firstLetter not in self.children:
        return False

      return self.children[firstLetter].search(rest, isEntireMatch)

class Trie:
    def __init__(self):
      self.root = Node()

    def insert(self, word: str) -> None:
      self.root.insert(word)


    def search(self, word: str) -> bool:
      return self.root.search(word, True)

    def startsWith(self, prefix: str) -> bool:
      return self.root.search(prefix, False)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
