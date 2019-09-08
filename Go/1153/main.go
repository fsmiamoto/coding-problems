package main

import "fmt"

func fact(n int) int {
	if n == 0 {
		return 1
	}

	return n * fact(n-1)
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	fmt.Printf("%d\n", fact(n))
}
