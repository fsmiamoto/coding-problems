package main

import (
	"fmt"
	"strconv"
)

func main() {

	testNum := 1
	for {
		var n int
		var expr string
		for i := 0; i < 2; i++ {
			fmt.Scanf("%d", &n)

			if n == 0 {
				return
			}

			fmt.Scanf("%s", &expr)

			var result int
			var number []rune
			op := '+'

			for i := range expr {
				r := rune(expr[i])

				if r != '+' && r != '-' {
					number = append(number, r)
				} else {
					n, _ := strconv.Atoi(string(number))

					if op == '+' {
						result += n
					} else {
						result -= n
					}

					op = r
					number = []rune{}
				}
			}

			n, _ := strconv.Atoi(string(number))
			if op == '+' {
				result += n
			} else {
				result -= n
			}

			fmt.Println("Teste", testNum)
			fmt.Println(result)
			fmt.Println()

			testNum++
		}
	}
}
