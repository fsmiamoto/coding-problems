package main

import "fmt"

func main() {
	var period int
	fmt.Scanf("%d", &period)

	for i := 0; i < 1000; i++ {
		fmt.Printf("N[%d] = %d\n", i, i%period)
	}
}
