package main

import "fmt"

func main() {
	var numOfLinhas int
	fmt.Scanf("%d", &numOfLinhas)

	for i := 0; i < numOfLinhas; i++ {
		fmt.Printf("%d %d %d PUM\n", 1+4*i, 2+4*i, 3+4*i)
	}
}
