package main

import "fmt"

func main() {
	var arr [20]int

	for i := 0; i < 20; i++ {
		var x int
		fmt.Scanf("%d", &x)

		arr[19-i] = x
	}

	for i, v := range arr {
		fmt.Printf("N[%d] = %d\n", i, v)
	}
}
