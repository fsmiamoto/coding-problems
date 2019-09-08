package main

import "fmt"

func fib(n int) int {
	if n == 1 {
		return 0
	}
	if n == 2 {
		return 1
	}

	return fib(n-2) + fib(n-1)
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	for i := 1; i <= n; i++ {
		if i == n {
			fmt.Printf("%d\n", fib(i))
			continue
		}

		fmt.Printf("%d ", fib(i))
	}
}
