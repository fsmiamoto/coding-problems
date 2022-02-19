package main

import "fmt"

func main() {
	sum, n := 0, 0
	for {
		var idade int
		fmt.Scanf("%d", &idade)
		if idade < 0 {
			break
		}
		sum += idade
		n++
	}

	fmt.Printf("%.2f\n", float32(sum)/float32(n))
}
