package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		var x int64

		_, err := fmt.Scanf("%d", &x)
		if err != nil {
			break
		}

		x++

		if x%2 == 0 || x%7 != 0 {
			fmt.Println("No")
			continue
		}

		i := big.NewInt(x + 2)
		isPrime := i.ProbablyPrime(1)

		if isPrime {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}

	}
}
