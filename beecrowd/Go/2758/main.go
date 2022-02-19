package main

import "fmt"

func main() {
	var a, b float32
	var c, d float64

	fmt.Scanf("%f", &a)
	fmt.Scanf("%f", &b)
	fmt.Scanf("%f", &c)
	fmt.Scanf("%f", &d)

	fmt.Printf("A = %.6f, B = %.6f\n", a, b)
	fmt.Printf("C = %.6f, D = %.6f\n", c, d)

	fmt.Printf("A = %.1f, B = %.1f\n", a, b)
	fmt.Printf("C = %.1f, D = %.1f\n", c, d)

	fmt.Printf("A = %.2f, B = %.2f\n", a, b)
	fmt.Printf("C = %.2f, D = %.2f\n", c, d)

	fmt.Printf("A = %.3f, B = %.3f\n", a, b)
	fmt.Printf("C = %.3f, D = %.3f\n", c, d)

	fmt.Printf("A = %.3E, B = %.3E\n", a, b)
	fmt.Printf("C = %.3E, D = %.3E\n", c, d)

	fmt.Printf("A = %.0f, B = %.0f\n", a, b)
	fmt.Printf("C = %.0f, D = %.0f\n", c, d)
}
