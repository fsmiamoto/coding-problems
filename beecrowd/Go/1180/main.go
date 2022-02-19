package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	smallest, index := math.MaxInt32, 0

	for i := 0; i < n; i++ {
		var x int
		fmt.Scanf("%d", &x)

		if x < smallest {
			smallest = x
			index = i
		}
	}

	fmt.Printf("Menor valor: %d\n", smallest)
	fmt.Printf("Posicao: %d\n", index)
}
