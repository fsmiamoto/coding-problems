package main

import "fmt"

func main() {
	for {
		var n int
		_, err := fmt.Scanf("%d", &n)
		if err != nil {
			break
		}

		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {

				switch {
				case i+j == n-1:
					fmt.Print(2)
				case i == j:
					fmt.Print(1)
				default:
					fmt.Print(3)
				}

				if j == n-1 {
					fmt.Println()
				}
			}
		}
	}
}
