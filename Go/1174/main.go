package main

import "fmt"

func main() {
	for i := 0; i < 100; i++ {
		var x float32
		fmt.Scanf("%f", &x)

		if x <= 10 {
			fmt.Printf("A[%d] = %.1f\n", i, x)
		}
	}
}
