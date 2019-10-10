package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 0; i < n-1; i++ {
		fmt.Print("Ho ")
	}
	fmt.Println("Ho!")
}
