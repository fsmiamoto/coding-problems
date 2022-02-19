package main

import "fmt"
import "math"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 1; i < n+1; i++ {
		j := float64(i)
		fmt.Printf("%v %v %v\n", j, math.Pow(j, 2), math.Pow(j, 3))
	}
}
