package main

import "fmt"

func main() {
	n, a := 0, 0

	fmt.Scanf("%d", &n)

	// Reads until a positive integer is found
	for {
		fmt.Scanf("%d", &a)
		if a > 0 {
			break
		}
	}

	sum := 0
	for i := 0; i < a; i++ {
		sum += n + i
	}

	fmt.Println(sum)
}
