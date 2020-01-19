package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int

	for {
		fmt.Scanf("%d", &n)

		if n == 0 {
			break
		}

		digits := strconv.Itoa(1 << uint(2*(n-1)))
		format := fmt.Sprintf("%%%d", len(digits))

		for i := 0; i < n; i++ {
			base := 1 << uint(i)
			for j := 0; j < n; j++ {
				fmt.Printf(format+"d", base<<uint(j))
				if j == n-1 {
					fmt.Println()
				} else {
					fmt.Print(" ")
				}
			}
		}

		fmt.Println()
	}
}
