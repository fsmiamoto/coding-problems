package main

import "fmt"

type Node struct {
	Key         int
	Left, Right *Node
}

func (n *Node) Insert(key int) {
	if n.Key < key {
		if n.Right == nil {
			n.Right = &Node{Key: key}
		} else {
			n.Right.Insert(key)
		}
		return
	}

	if n.Left == nil {
		n.Left = &Node{Key: key}
	} else {
		n.Left.Insert(key)
	}
}

func (n *Node) Search(key int) bool {
	if n == nil {
		return false
	}

	if n.Key < key {
		return n.Right.Search(key)
	}

	return n.Left.Search(key)
}

func main() {
	tree := &Node{Key: 100}

	tree.Insert(50)
	tree.Insert(49)
	tree.Insert(48)
	tree.Insert(53)
	tree.Insert(7)

	fmt.Println(tree)
	fmt.Println(tree.Search(7))
	fmt.Println(tree.Search(100))
}
