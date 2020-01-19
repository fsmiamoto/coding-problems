package main

import "fmt"

func main() {
	var n int64
	fmt.Scanf("%d", &n)

	a := n * (n - 1)
	b := a * (n - 2) * (n - 3)

	fmt.Println(1 + a/2 + b/24)
}
