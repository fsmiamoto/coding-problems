package main

import "fmt"

func main() {
	var N int
	fmt.Scanf("%d", &N)

	for n := 0; n < N; n++ {

		var x int
		var sum int
		fmt.Scanf("%d", &x)

		for i := 1; i < x; i++ {
			if x%i == 0 {
				sum += i
			}
		}

		if sum != x {
			fmt.Printf("%d nao eh perfeito\n", x)
			continue
		}

		fmt.Printf("%d eh perfeito\n", x)
	}

}
