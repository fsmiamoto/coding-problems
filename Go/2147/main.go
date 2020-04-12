package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		var s string
		fmt.Scanf("%s", &s)

		fmt.Printf("%.2f\n", 0.01*float32(len(s)))
	}
}
