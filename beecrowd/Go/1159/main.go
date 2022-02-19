package main

import "fmt"

func main() {
	for {
		var n int64

		fmt.Scanf("%d", &n)

		if n == 0 {
			break
		}

		sum := n
		nextEven := n + 2

		if n%2 == 1 {
			sum += 1
			nextEven += 1
		}

		for i := 0; i < 4; i++ {
			sum += nextEven
			nextEven += 2
		}

		fmt.Println(sum)
	}
}
