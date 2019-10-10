package main

import "fmt"

func main() {
	var x, z int

	fmt.Scanf("%d", &x)

	for {
		fmt.Scanf("%d", &z)
		if x < z {
			break
		}
	}

	sum := x
	steps := 1

	for sum < z {
		sum += x + (x + steps)
		steps++
	}

	fmt.Println(steps + 1)
}
