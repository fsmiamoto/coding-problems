package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

// MaxHeap

type MaxHeap[T constraints.Ordered] struct {
	array []T
}

func (h *MaxHeap[T]) Insert(key T) {
	h.array = append(h.array, key)
	h.heapifyUp(len(h.array) - 1)
}

func (h *MaxHeap[T]) Extract() T {
	if len(h.array) == 0 {
		panic("empty heap")
	}

	extracted := h.array[0]

	last := len(h.array) - 1
	h.array[0] = h.array[last]
	h.array = h.array[:last]

	h.heapifyUp(len(h.array) - 1)

	return extracted
}

func (h *MaxHeap[T]) heapifyUp(index int) {
	for h.array[parent(index)] < h.array[index] {
		h.swap(parent(index), index)
		index = parent(index)
	}
}

func (h *MaxHeap[T]) heapifyDown(index int) {
	lastIndex := len(h.array) - 1

	l, r := left(index), right(index)
	childToCompare := 0

	for l <= lastIndex {
		if l == lastIndex {
			childToCompare = l
		} else if h.array[l] > h.array[r] {
			childToCompare = l
		} else {
			childToCompare = r
		}

		if h.array[index] < h.array[childToCompare] {
			h.swap(index, childToCompare)
			index = childToCompare
			l, r = left(index), right(index)
		} else {
			return
		}
	}
}

func (h *MaxHeap[T]) swap(i, j int) {
	h.array[i], h.array[j] = h.array[j], h.array[i]
}

func parent(index int) int {
	return (index - 1) / 2
}

func left(index int) int {
	return 2*index + 1
}

func right(index int) int {
	return 2*index + 1
}

func main() {
	heap := &MaxHeap[int]{}

	heap.Insert(1)
	heap.Insert(3)
	heap.Insert(4)
	heap.Insert(8)
	heap.Insert(2)

	fmt.Println(heap.Extract())
}
