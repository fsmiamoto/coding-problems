package main

import "fmt"

func main() {
	var avg, grade int

	fmt.Scanf("%d", &grade)
	fmt.Scanf("%d", &avg)

	fmt.Println(avg*2 - grade)
}
