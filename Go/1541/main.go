package main

import (
	"fmt"
	"math"
)

func main() {
	for {
		var h, l, p float64
		_, err := fmt.Scanf("%f %f %f", &l, &h, &p)

		if err != nil {
			break
		}
		result := math.Sqrt((100.0 / p) * h * l)
		fmt.Println(int(result))
	}
}
