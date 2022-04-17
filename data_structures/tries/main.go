package main

import "fmt"

const AlphabetSize = 26

type Node struct {
	children [AlphabetSize]*Node
	isEnd    bool
}

type Trie struct {
	root *Node
}

func (n *Node) insert(word string) {
	if len(word) == 0 {
		n.isEnd = true
		return
	}
	firstLetter, rest := word[0], word[1:]

	index := firstLetter - 'a'
	if n.children[index] == nil {
		// Initialize children
		n.children[index] = &Node{}
	}

	n.children[index].insert(rest)
}

func (n *Node) search(word string) bool {
	if len(word) == 0 {
		return n.isEnd
	}

	firstLetter, rest := word[0], word[1:]

	index := firstLetter - 'a'
	if n.children[index] == nil {
		return false
	}

	return n.children[index].search(rest)
}

func NewTrie() *Trie {
	return &Trie{
		root: &Node{},
	}
}

func (t *Trie) Insert(word string) {
	t.root.insert(word)
}

func (t *Trie) Search(word string) bool {
	return t.root.search(word)
}

func main() {
	trie := NewTrie()

	trie.Insert("hello")
	trie.Insert("hell")
	trie.Insert("ola")
	trie.Insert("tudo")
	trie.Insert("bem")

	fmt.Println(trie.Search("hello"))
	fmt.Println(trie.Search("hell"))
	fmt.Println(trie.Search("he"))
	fmt.Println(trie.Search("helloo"))
	fmt.Println(trie.Search("bem"))
	fmt.Println(trie.Search("oi"))
}
