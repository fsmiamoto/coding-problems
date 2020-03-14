package main

import "fmt"

func main() {
	for {
		var n int
		_, err := fmt.Scanf("%d", &n)

		if err != nil {
			break
		}

		if n > 0 {
			fmt.Println("vai ter duas!")
			continue
		}

		fmt.Println("vai ter copa!")
	}
}
