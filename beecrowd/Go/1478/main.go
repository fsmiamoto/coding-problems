package main

import "fmt"

func main() {
	var n int
	for {
		fmt.Scanf("%d", &n)

		if n == 0 {
			break
		}

		for i := 0; i < n; i++ {
			printDecrescente(i + 1)
			printCrescente(n - i + 1)
		}

		fmt.Println()
	}
}

func printDecrescente(n int) {
	for i := n; i > 1; i-- {
		fmt.Printf("%3d ", i)
	}
}

func printCrescente(n int) {
	for i := 1; i < n; i++ {
		fmt.Printf("%3d", i)
		if i == n-1 {
			fmt.Println()
		} else {
			fmt.Print(" ")
		}
	}
}
