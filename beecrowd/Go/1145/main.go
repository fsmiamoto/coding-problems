package main

import "fmt"

func main() {
	var numCols, maxCount int
	count := 1
	fmt.Scanf("%d %d", &numCols, &maxCount)
	for count <= maxCount {
		for i := 0; i < numCols; i++ {
			fmt.Printf("%d", count)
			count++
			if i < numCols-1 {
				fmt.Printf(" ")
			}
		}
		fmt.Printf("\n")
	}

}
