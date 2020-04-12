package main

import "fmt"

func main() {
	var valor, parcelas int

	fmt.Scanf("%d\n%d", &valor, &parcelas)

	p := valor / parcelas
	resto := valor % parcelas

	for i := 0; i < resto; i++ {
		fmt.Println(p + 1)
	}
	for i := 0; i < parcelas-resto; i++ {
		fmt.Println(p)
	}
}
