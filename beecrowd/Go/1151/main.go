package main

import "fmt"

// Prints n first number of the Fibonacci sequence until n
func printFib(n int) {
	lastTwo := []int64{0, 1}
	counter := 1
	for counter <= n {
		fmt.Printf("%d", lastTwo[0])

		// Gets next fib number
		nextFib := lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib

		if counter != n {
			fmt.Print(" ")
		} else {
			fmt.Print("\n")
		}

		counter++
	}
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	printFib(n)
}
