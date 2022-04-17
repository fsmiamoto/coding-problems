package main

import "fmt"

const ArraySize = 10

type HashTable struct {
	array [ArraySize]*bucket
}

// Insert adds a key to the hash map
// this does not deal well with duplicated keys in a bucket
func (h *HashTable) Insert(key string) {
	index := hash(key)
	h.array[index].insert(key)
}

func (h *HashTable) Search(key string) bool {
	index := hash(key)
	return h.array[index].search(key)
}

func (h *HashTable) Delete(key string) {
	index := hash(key)
	h.array[index].delete(key)
}

// hash hashes a given key
func hash(key string) int {
	sum := 0
	for i := range key {
		sum += int(key[i])
	}
	return sum % ArraySize
}

type bucket struct {
	head *bucketNode
}

func (b *bucket) insert(key string) {
	node := &bucketNode{key, nil}
	node.next = b.head
	b.head = node
}

func (b *bucket) search(key string) bool {
	node := b.head
	for node != nil {
		if node.key == key {
			return true
		}
		node = node.next
	}
	return false
}

func (b *bucket) delete(key string) {
	prev, node := (*bucketNode)(nil), b.head
	for node != nil {
		if node.key == key {
			// Found it
			if prev == nil {
				// First node
				b.head = node.next
			} else {
				prev.next = node.next
			}
			return
		}
		prev, node = node, node.next
	}
}

type bucketNode struct {
	key  string
	next *bucketNode
}

func NewHashTable() *HashTable {
	ht := &HashTable{}
	for i := range ht.array {
		ht.array[i] = &bucket{}
	}
	return ht
}

func main() {
	hashTable := NewHashTable()

	hashTable.Insert("joaozinho")

	fmt.Println(hashTable.Search("joaozinho"))
	fmt.Println(hashTable.Search("fulano"))

	hashTable.Delete("joaozinho")
	hashTable.Insert("fulano")
	hashTable.Insert("ciclano")

	fmt.Println(hashTable.Search("joaozinho"))
	fmt.Println(hashTable.Search("fulano"))
	fmt.Println(hashTable.Search("ciclano"))
	fmt.Println(hashTable.Search("beltrano"))
}
