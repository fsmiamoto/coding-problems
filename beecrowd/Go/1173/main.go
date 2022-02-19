package main

import (
	"fmt"
	"math"
)

func main() {
	var x int
	fmt.Scanf("%d", &x)

	for i := 0; i < 10; i++ {
		fmt.Printf("N[%d] = %d\n", i, x*int(math.Pow(2.0, float64(i))))
	}
}
