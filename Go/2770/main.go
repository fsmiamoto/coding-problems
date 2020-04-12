package main

import "fmt"

func main() {
	for {
		var w, h, n int

		_, err := fmt.Scanf("%d %d %d", &w, &h, &n)

		if err != nil {
			break
		}

		for i := 0; i < n; i++ {
			var x, y int
			fmt.Scanf("%d %d", &x, &y)

			if (x <= w && y <= h) || (x <= h && y <= w) {
				fmt.Println("Sim")
				continue
			}

			fmt.Println("Nao")

		}
	}
}
