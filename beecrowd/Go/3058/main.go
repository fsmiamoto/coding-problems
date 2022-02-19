package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	var min float64

	for i := 0; i < n; i++ {
		var price, grams float64
		fmt.Scanf("%f %f", &price, &grams)

		total := (1000.0 / grams) * price

		if total < min || i == 0 {
			min = total
			continue
		}
	}

	fmt.Printf("%.2f\n", min)
}
