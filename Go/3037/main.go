package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		joao := 0
		for i := 0; i < 3; i++ {
			var x, d int
			fmt.Scanf("%d %d", &x, &d)
			joao += x * d
		}

		maria := 0
		for i := 0; i < 3; i++ {
			var x, d int
			fmt.Scanf("%d %d", &x, &d)
			maria += x * d
		}

		if maria > joao {
			fmt.Println("MARIA")
		} else {
			fmt.Println("JOAO")
		}
	}
}
