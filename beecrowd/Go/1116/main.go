package main

import "fmt"

func main() {
	var numOfTests int
	fmt.Scanf("%d", &numOfTests)

	var a, b int
	for i := 0; i < numOfTests; i++ {
		fmt.Scanf("%d %d", &a, &b)
		if b == 0 {
			fmt.Println("divisao impossivel")
			continue
		}

		result := float32(a) / float32(b)
		fmt.Printf("%.1f\n", result)
	}
}
