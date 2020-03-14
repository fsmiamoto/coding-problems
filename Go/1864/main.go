package main

import "fmt"

const msg = "LIFE IS NOT A PROBLEM TO BE SOLVED"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	fmt.Println(msg[:n])
}
