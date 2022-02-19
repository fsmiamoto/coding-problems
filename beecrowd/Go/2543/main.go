package main

import "fmt"

const (
	cs = iota
	lol
)

func main() {
	var yourId int
	var n, count int

	fmt.Println(cs)
	fmt.Println(lol)

	fmt.Scanf("%d %d", &n, &yourId)

	for i := 0; i < n; i++ {
		var id, game int
		fmt.Scanf("%d %d", &id, &game)

		if id != yourId || game != cs {
			continue
		}

		count++
	}

	fmt.Println(count)
}
