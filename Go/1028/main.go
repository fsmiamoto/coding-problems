// 1028 - Figurinhas
package main

import "fmt"

func main() {
	var numOfTests int
	var a, b int
	fmt.Scanf("%d", &numOfTests)

	for i := 0; i < numOfTests; i++ {
		fmt.Scanf("%d %d", &a, &b)

		// Euclidian algorithm
		for a != b {
			if a > b {
				a -= b
			} else {
				b -= a
			}
		}

		fmt.Println(a)
	}
}
