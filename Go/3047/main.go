package main

import "fmt"

func main() {
	var m, a, b int

	fmt.Scanf("%d", &m)
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)

	oldest := m - a - b
	if a > oldest {
		oldest = a
	}
	if b > oldest {
		oldest = b
	}

	fmt.Println(oldest)
}
