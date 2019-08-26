package main

import "fmt"

func main() {
	var numOfTests, n int
	var fib int64
	fmt.Scanf("%d", &numOfTests)

	for i := 0; i < numOfTests; i++ {
		fmt.Scanf("%d", &n)
		fib = fibonacci(n)
		fmt.Println(fib)
	}

	fmt.Print("Oi\n")
}

func fibonacci(n int) int64 {
	a, b := 0, 1
	for i := 0; i < n; i++ {

	}

}
