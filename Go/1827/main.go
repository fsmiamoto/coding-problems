package main

import "fmt"

func main() {
	var n int

	for {
		_, err := fmt.Scanf("%d", &n)
		if err != nil {
			break
		}

		half := n / 2
		xBound, yBound := n/3, n-n/3-1

		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				switch {
				case i == half && j == half:
					fmt.Print(4)
				case i >= xBound && i <= yBound && j >= xBound && j <= yBound:
					fmt.Print(1)
				case i == j:
					fmt.Print(2)
				case i+j == n-1:
					fmt.Print(3)
				default:
					fmt.Print(0)
				}

			}
			fmt.Println()
		}
		fmt.Println()
	}
}
