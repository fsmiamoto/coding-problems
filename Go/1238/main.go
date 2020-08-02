package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	var a, b string
	var j, k int

	for i := 0; i < n; i++ {
		fmt.Scanf("%s %s", &a, &b)

		for j, k = 0, 0; j < len(a) && k < len(b); {
			fmt.Printf("%c%c", a[j], b[k])
			j++
			k++
		}

		for ; j < len(a); j++ {
			fmt.Printf("%c", a[j])
		}

		for ; k < len(b); k++ {
			fmt.Printf("%c", b[k])
		}

		fmt.Println()
	}
}
