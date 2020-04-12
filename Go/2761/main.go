package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var i int
	var f float32
	var r string
	var s string

	fmt.Scanf("%d %f %s", &i, &f, &r)

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	s = scanner.Text()

	fmt.Printf("%d%.6f%s%s\n", i, f, r, s)
	fmt.Printf("%d\t%.6f\t%s\t%s\n", i, f, r, s)
	fmt.Printf("%10d%10.6f%10s%10s\n", i, f, r, s)
}
