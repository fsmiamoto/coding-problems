package main

import (
	"fmt"
	"math"
)

func main() {
	i := 0.0

	for i <= 2.0 {
		if i == 0.0 || i == 1.0 || math.Abs(i-2.0) <= 0.2 {
			fmt.Printf("I=%.g J=%d\n", i, 1)
			fmt.Printf("I=%.g J=%d\n", i, 2)
			fmt.Printf("I=%.g J=%d\n", i, 3)
			i += 0.2
			continue
		}

		fmt.Printf("I=%1.1f J=%d\n", i, 1)
		fmt.Printf("I=%1.1f J=%d\n", i, 2)
		fmt.Printf("I=%1.1f J=%d\n", i, 3)
		i += 0.2
	}
}
