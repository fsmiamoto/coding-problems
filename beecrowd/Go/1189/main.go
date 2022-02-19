package main

import "fmt"

func main() {
	var sum float64

	var op string
	fmt.Scanf("%s", &op)

	// Read the matrix
	for i := 0; i < 12; i++ {
		for j := 0; j < 12; j++ {
			var x float64
			fmt.Scanf("%f", &x)

			if j >= 5 {
				continue
			}

			if j < i && j < 11-i {
				sum += x
			}

		}
	}

	switch op {
	case "S":
		fmt.Printf("%.1f\n", sum)
	case "M":
		fmt.Printf("%.1f\n", sum/float64(30))
	}
}
