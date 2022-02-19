package main

import "fmt"

func main() {
	var numOfCases int
	fmt.Scanf("%d", &numOfCases)

	for i := 0; i < numOfCases; i++ {
		var x int
		fmt.Scanf("%d", &x)

		fmt.Printf("Fib(%d) = %d\n", x, fib(x))
	}
}

// Gets the (n+1)th number in the Fibonacci sequence
func fib(n int) int64 {
	if n == 0 {
		return 0
	}

	if n == 1 {
		return 1
	}

	lastTwo := []int64{0, 1}
	counter := 2
	for counter <= n {
		nextFib := lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter++
	}

	return lastTwo[1]
}
