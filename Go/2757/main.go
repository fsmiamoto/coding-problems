package main

import "fmt"

func main() {
	var a, b, c int

	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)
	fmt.Scanf("%d", &c)

	fmt.Printf("A = %d, B = %d, C = %d\n", a, b, c)
	fmt.Printf("A = %10d, B = %10d, C = %10d\n", a, b, c)
	fmt.Printf("A = %010d, B = %010d, C = %010d\n", a, b, c)
	fmt.Printf("A = %-10d, B = %-10d, C = %-10d\n", a, b, c)
}
