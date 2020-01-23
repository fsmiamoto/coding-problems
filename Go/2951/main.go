package main

import "fmt"

func main() {
	var numOfRunes, minFriendship int

	fmt.Scanf("%d %d", &numOfRunes, &minFriendship)

	runes := make(map[string]int)
	for i := 0; i < numOfRunes; i++ {
		var s string
		var n int
		fmt.Scanf("%s %d", &s, &n)
		runes[s] = n
	}

	var numOfRunesUsed int
	fmt.Scanf("%d", &numOfRunesUsed)

	total := 0
	for i := 0; i < numOfRunesUsed; i++ {
		var s string
		fmt.Scanf("%s", &s)
		total += runes[s]
	}

	fmt.Println(total)

	if total == minFriendship {
		fmt.Println("You shall pass!")
		return
	}
	fmt.Println("My precioooous")
}
