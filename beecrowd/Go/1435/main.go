package main

import "fmt"

func main() {
	var n int
	for {
		fmt.Scanf("%d", &n)

		if n == 0 {
			break
		}

		for i := 1; i <= n; i++ {
			for j := 1; j <= n; j++ {
				var maior, menor int

				if i > j {
					maior, menor = i, j
				} else {
					maior, menor = j, i
				}

				valor := 1

				if a, b := menor-1, n-maior; a < b {
					valor += a
				} else {
					valor += b
				}

				fmt.Printf("%3d", valor)

				if j == n {
					fmt.Println()
					continue
				}

				fmt.Print(" ")
			}
		}

		fmt.Println()
	}
}
