package main

import "fmt"

func main() {
	for {
		var n int
		_, err := fmt.Scanf("%d", &n)
		if err != nil {
			break
		}

		num, den := 0, 0
		for i := 0; i < n; i++ {
			var grade, weight int
			fmt.Scanf("%d %d", &grade, &weight)

			num += grade * weight
			den += weight
		}

		ira := float64(num) / (float64(den) * 100)
		fmt.Printf("%.4f\n", ira)
	}
}
