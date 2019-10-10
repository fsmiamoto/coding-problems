package main

import (
	"fmt"
)

func main() {
	var n int
	var popA, popB int64
	var growthA, growthB float64

	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {

		fmt.Scanf("%d %d %1.f %.1f", &popA, &popB, &growthA, &growthB)

		years := 1
		gA := 1.0 + growthA/100.0
		gB := 1.0 + growthB/100.0

		for {
			popA2 := float64(popA) * gA
			popB2 := float64(popB) * gB

			fmt.Println(popA)
			fmt.Println(popB)

			if popA > popB {
				break
			}
			years++
		}

		if years > 100 {
			fmt.Printf("Mais de 1 seculo.")
			continue
		}

		fmt.Printf("%d anos", years)
	}

}
