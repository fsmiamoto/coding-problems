package main

import "fmt"

func main() {
	var numOfCases int
	fmt.Scanf("%d", &numOfCases)

	for i := 0; i < numOfCases; i++ {
		var x int
		fmt.Scanf("%d", &x)

		result, calls := fib(x)

		fmt.Printf("fib(%d) = %d calls = %d\n", x, calls, result)
	}
}

// Gets the (n+1)th number and the number of recursive calls in the Fibonacci sequence
func fib(n int) (int64, int64) {
	if n == 0 {
		return 0, 0
	}

	if n == 1 {
		return 1, 0
	}

	lastTwoResults := []int64{0, 1}
	lastTwoCalls := []int64{0, 0}
	counter := 2

	for counter <= n {
		nextFib := lastTwoResults[0] + lastTwoResults[1]
		nextCalls := lastTwoCalls[0] + lastTwoCalls[1] + 2

		lastTwoResults[0] = lastTwoResults[1]
		lastTwoResults[1] = nextFib

		lastTwoCalls[0] = lastTwoCalls[1]
		lastTwoCalls[1] = nextCalls

		counter++
	}

	return lastTwoResults[1], lastTwoCalls[1]
}
