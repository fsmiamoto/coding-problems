package main

import (
	"fmt"
	"math"
)

func main() {
	var x float64
	fmt.Scanf("%f", &x)

	for i := 0; i < 100; i++ {
		fmt.Printf("N[%d] = %.4f\n", i, x/math.Pow(2.0, float64(i)))
	}

}
