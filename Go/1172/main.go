package main

import "fmt"

func main() {
	for i := 0; i < 10; i++ {
		var x int
		fmt.Scanf("%d", &x)

		if x <= 0 {
			x = 1
		}

		fmt.Printf("X[%d] = %d\n", i, x)
	}
}
