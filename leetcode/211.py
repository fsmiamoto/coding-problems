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

    def search(self, word: str) -> bool:
      if len(word) == 0:
        return self.isEnd

      firstLetter, rest = word[0], word[1:]
      if firstLetter == '.':
        matched = False
        # Search for rest in each children
        for children in self.children.values():
          matched = matched or children.search(rest)
        return matched
      elif firstLetter not in self.children:
        return False

      return self.children[firstLetter].search(rest)

class Trie:
    def __init__(self):
      self.root = Node()

    def insert(self, word: str) -> None:
      self.root.insert(word)


    def search(self, word: str) -> bool:
      return self.root.search(word)

class WordDictionary:
    def __init__(self):
      self.trie = Trie()

    def addWord(self, word: str) -> None:
      self.trie.insert(word)


    def search(self, word: str) -> bool:
      return self.trie.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
