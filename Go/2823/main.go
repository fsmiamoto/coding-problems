package main

import "fmt"

func main() {
	var n int

	fmt.Scanf("%d", &n)

	total := 0.0
	for i := 0; i < n; i++ {
		var c, t float64
		fmt.Scanf("%f %f", &c, &t)
		total += c / t
	}

	if total > 1 {
		fmt.Println("FAIL")
	} else {
		fmt.Println("OK")
	}
}
