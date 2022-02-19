package main

import "fmt"

func main() {
	var N int
	fmt.Scanf("%d", &N)

	for i := 0; i < N; i++ {
		var x, y int

		fmt.Scanf("%d %d", &x, &y)

		sum := x
		nextOdd := x + 2

		if x%2 == 0 {
			sum += 1
			nextOdd += 1
		}

		for j := 0; j < y-1; j++ {
			sum += nextOdd
			nextOdd += 2
		}

		fmt.Println(sum)
	}

}
