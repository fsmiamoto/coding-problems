package main

import "fmt"

func main() {
	sum := float64(0)
	for i := 0; i < 100; i++ {
		sum += float64(1) / float64(i+1)
	}

	fmt.Printf("%.2f\n", sum)
}
