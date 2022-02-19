package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)
	for n != 0 {
		for i := 1; i < n; i++ {
			fmt.Printf("%d ", i)
		}
		fmt.Printf("%d\n", n)
		fmt.Scanf("%d", &n)
	}
}
