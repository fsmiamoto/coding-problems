package main

import (
	"fmt"
	"math"
)

func main() {
	sum := float64(0)
	for i := 0; i < 20; i++ {
		sum += float64(2*i+1) / math.Pow(2, float64(i))
	}

	fmt.Printf("%.2f\n", sum)
}
