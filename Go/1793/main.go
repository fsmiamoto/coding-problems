package main

import "fmt"

func main() {
	for {
		var n int
		fmt.Scanf("%d", &n)

		if n == 0 {
			break
		}

		timestamps := make([]int, n)

		for i := 0; i < n; i++ {
			fmt.Scanf("%d", &timestamps[i])
		}

		total := 0
		for i := 0; i < n-1; i++ {
			if timestamps[i+1]-timestamps[i] > 10 {
				total += 10
			} else {
				total += timestamps[i+1] - timestamps[i]
			}
		}
		total += 10

		fmt.Println(total)
	}
}
